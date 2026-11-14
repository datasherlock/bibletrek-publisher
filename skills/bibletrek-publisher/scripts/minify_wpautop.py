#!/usr/bin/env python3
"""
Minifies Bible Trek HTML payloads into a single wpautop-safe line and validates against:
1. Block elements (<div>, <h1>-<h6>, <p>, <ul>, <ol>) nested inside inline <a> or <span> tags
   (which causes WordPress wpautop to split cards into ghost grid cells!).
2. <style> blocks placed at the beginning of [fusion_text] instead of at the end.
3. Localhost or insecure http://bibletrek4kids.com image URLs.

Usage:
  python3 minify_wpautop.py <input_html_or_txt_file> [--in-place]
"""
import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

BLOCK_TAGS = {"div", "h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "ol", "table", "section", "article", "blockquote"}
INLINE_CONTAINERS = {"a", "span"}


class WpautopSafetyValidator(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_l = tag.lower()
        if tag_l in BLOCK_TAGS:
            for anc in self.stack:
                if anc in INLINE_CONTAINERS:
                    self.errors.append(
                        f"Illegal block <{tag_l}> nested inside inline <{anc}> (line {self.getpos()[0]}). "
                        f"Use a <div style='position:relative'> card with a stretched <h3><a class='...-stretch'> instead!"
                    )
        if tag_l == "img":
            attr_map = dict(attrs)
            src = attr_map.get("src") or ""
            if "localhost" in src or src.startswith("http://"):
                self.errors.append(f"Insecure or localhost <img> src detected: {src}")
            if "alt" not in attr_map or not (attr_map.get("alt") or "").strip():
                self.errors.append(f"Missing descriptive alt attribute on <img src='{src[:60]}'>")
        if tag_l not in {"br", "img", "hr", "meta", "link", "input", "source", "path", "circle", "rect", "line", "polygon", "polyline"}:
            self.stack.append(tag_l)

    def handle_endtag(self, tag: str) -> None:
        tag_l = tag.lower()
        if tag_l in self.stack:
            while self.stack:
                popped = self.stack.pop()
                if popped == tag_l:
                    break


def minify_payload(raw: str) -> str:
    s = re.sub(r"\s*\n\s*", " ", raw.strip())
    s = re.sub(r">\s+<", "><", s)
    return s


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and minify Bible Trek Avada/HTML payload.")
    parser.add_argument("file", help="Path to HTML/Fusion shortcode payload file")
    parser.add_argument("--in-place", action="store_true", help="Overwrite input file with minified output")
    args = parser.parse_args()

    path = Path(args.file).expanduser().resolve()
    raw = path.read_text(encoding="utf-8")

    validator = WpautopSafetyValidator()
    validator.feed(raw)

    ft_start = raw.find("[fusion_text")
    style_pos = raw.find("<style")
    if ft_start != -1 and style_pos != -1 and style_pos < raw.find("<div", ft_start):
        validator.errors.append(
            "<style> appears before content inside [fusion_text]. Move <style>...</style> right before [/fusion_text] so snippets never scrape CSS."
        )

    if validator.errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for err in validator.errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)

    minified = minify_payload(raw)
    if args.in_place:
        path.write_text(minified, encoding="utf-8")
        print(f"[OK] Validated and minified in-place: {path} ({len(minified)} bytes, 0 wpautop hazards)")
    else:
        print(minified)


if __name__ == "__main__":
    main()
