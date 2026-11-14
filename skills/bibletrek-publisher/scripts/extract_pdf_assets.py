#!/usr/bin/env python3
"""
Cross-platform (Linux + macOS) PDF text extractor & PNG page renderer for Bible Trek.
Automatically tries PyMuPDF (fitz), pypdf/pypdfium2, poppler (pdftotext + pdftoppm), or macOS Swift PDFKit.

Usage:
  python3 extract_pdf_assets.py <pdf_file_or_directory> <output_dir> [--dpi 180]
"""
import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def extract_with_poppler(pdf_path: Path, out_dir: Path, dpi: int) -> dict:
    txt_file = out_dir / f"{pdf_path.stem}.txt"
    subprocess.run(["pdftotext", "-layout", str(pdf_path), str(txt_file)], check=True)
    text = txt_file.read_text(encoding="utf-8", errors="replace")

    img_prefix = out_dir / "pages" / pdf_path.stem
    img_prefix.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(dpi), str(pdf_path), str(img_prefix)],
        check=True,
    )
    pages = sorted(str(p) for p in img_prefix.parent.glob(f"{pdf_path.stem}-*.png"))
    return {"engine": "poppler", "text_file": str(txt_file), "char_count": len(text), "images": pages}


def extract_with_pymupdf(pdf_path: Path, out_dir: Path, dpi: int) -> dict:
    import fitz  # PyMuPDF

    doc = fitz.open(str(pdf_path))
    texts = []
    pages_dir = out_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    images = []
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    for idx, page in enumerate(doc, start=1):
        texts.append(f"--- PAGE {idx} ---\n" + page.get_text("text"))
        pix = page.get_pixmap(matrix=mat, alpha=False)
        img_out = pages_dir / f"{pdf_path.stem}-p{idx:02d}.png"
        pix.save(str(img_out))
        images.append(str(img_out))
    full_text = "\n\n".join(texts)
    txt_file = out_dir / f"{pdf_path.stem}.txt"
    txt_file.write_text(full_text, encoding="utf-8")
    return {"engine": "pymupdf", "text_file": str(txt_file), "char_count": len(full_text), "images": images}


def extract_with_macos_swift(pdf_path: Path, out_dir: Path, dpi: int) -> dict:
    pages_dir = out_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    swift_code = """
import Foundation
import PDFKit
import AppKit

let args = CommandLine.arguments
let pdfURL = URL(fileURLWithPath: args[1])
let txtPath = args[2]
let imgDir = args[3]
let scale = CGFloat(Double(args[4]) ?? 2.5)

guard let doc = PDFDocument(url: pdfURL) else { exit(1) }
var allText = ""
for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    allText += "--- PAGE \\(i+1) ---\\n" + (page.string ?? "") + "\\n\\n"
    let rect = page.bounds(for: .mediaBox)
    let w = Int(rect.width * scale)
    let h = Int(rect.height * scale)
    if let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h,
                                  bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true,
                                  isPlanar: false, colorSpaceName: .deviceRGB,
                                  bytesPerRow: 0, bitsPerPixel: 0) {
        NSGraphicsContext.saveGraphicsState()
        NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
        NSColor.white.set()
        NSRect(x: 0, y: 0, width: w, height: h).fill()
        let ctx = NSGraphicsContext.current!.cgContext
        ctx.scaleBy(x: scale, y: scale)
        page.draw(with: .mediaBox, to: ctx)
        NSGraphicsContext.restoreGraphicsState()
        if let png = rep.representation(using: .png, properties: [:]) {
            let outURL = URL(fileURLWithPath: imgDir).appendingPathComponent(String(format: "page-%02d.png", i+1))
            try? png.write(to: outURL)
        }
    }
}
try? allText.write(toFile: txtPath, atomically: true, encoding: .utf8)
"""
    txt_file = out_dir / f"{pdf_path.stem}.txt"
    stem_dir = pages_dir / pdf_path.stem
    stem_dir.mkdir(parents=True, exist_ok=True)
    swift_script = out_dir / "_extract.swift"
    swift_script.write_text(swift_code, encoding="utf-8")
    try:
        subprocess.run(
            ["/usr/bin/swift", str(swift_script), str(pdf_path), str(txt_file), str(stem_dir), str(dpi / 72.0)],
            check=True,
        )
    finally:
        swift_script.unlink(missing_ok=True)
    text = txt_file.read_text(encoding="utf-8", errors="replace")
    images = sorted(str(p) for p in stem_dir.glob("page-*.png"))
    return {"engine": "macos_swift_pdfkit", "text_file": str(txt_file), "char_count": len(text), "images": images}


def process_pdf(pdf_path: Path, out_dir: Path, dpi: int) -> dict:
    try:
        import fitz  # noqa: F401
        return extract_with_pymupdf(pdf_path, out_dir, dpi)
    except ImportError:
        pass

    if shutil.which("pdftotext") and shutil.which("pdftoppm"):
        return extract_with_poppler(pdf_path, out_dir, dpi)

    if platform.system() == "Darwin" and Path("/usr/bin/swift").exists():
        return extract_with_macos_swift(pdf_path, out_dir, dpi)

    raise RuntimeError(
        "No PDF backend found. Install PyMuPDF (`pip install pymupdf`) or poppler-utils (`apt install poppler-utils`)."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract verbatim text and high-res PNGs from Bible Trek PDFs.")
    parser.add_argument("source", help="Path to a PDF file or directory containing PDFs")
    parser.add_argument("output_dir", help="Output directory for extracted .txt and .png files")
    parser.add_argument("--dpi", type=int, default=180, help="Render DPI for PNG previews (default: 180)")
    args = parser.parse_args()

    src = Path(args.source).expanduser().resolve()
    out = Path(args.output_dir).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    pdfs = [src] if src.is_file() else sorted(src.rglob("*.pdf"))
    if not pdfs:
        print(f"No PDF files found at {src}", file=sys.stderr)
        sys.exit(1)

    manifest = {}
    for pdf in pdfs:
        rel_key = str(pdf.relative_to(src.parent if src.is_file() else src))
        manifest[rel_key] = process_pdf(pdf, out, args.dpi)
        print(f"[OK] {rel_key}: {manifest[rel_key]['char_count']} chars, {len(manifest[rel_key]['images'])} PNGs")

    manifest_path = out / "extraction_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Manifest saved to {manifest_path}")


if __name__ == "__main__":
    main()
