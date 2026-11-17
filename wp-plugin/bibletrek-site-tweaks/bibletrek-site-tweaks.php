<?php
/**
 * Plugin Name: Bible Trek Site Tweaks
 * Plugin URI: https://bibletrek4kids.com
 * Description: Lightweight frontend tweaks for Bible Trek 4 Kids: disables the post author byline across posts and archives, and cleanly left-aligns comment form checkboxes.
 * Version: 1.0.0
 * Author: Bible Trek 4 Kids
 * License: GPL-2.0-or-later
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Disable post author meta ("By Jerome Rajan") across Avada single posts and blog/category archives.
 */
add_filter(
	'option_fusion_options',
	function ( $options ) {
		if ( is_admin() || ! is_array( $options ) ) {
			return $options;
		}

		$options['post_meta_author'] = '0';

		foreach ( array( 'post_meta', 'blog_meta' ) as $meta_key ) {
			if ( isset( $options[ $meta_key ] ) && is_array( $options[ $meta_key ] ) ) {
				if ( array_key_exists( 'author', $options[ $meta_key ] ) ) {
					$options[ $meta_key ]['author'] = '0';
				} else {
					$options[ $meta_key ] = array_values( array_diff( $options[ $meta_key ], array( 'author' ) ) );
				}
			}
		}

		return $options;
	},
	20
);

/**
 * Output lightweight frontend CSS to ensure zero stray author bylines and crisp left-aligned comment checkboxes.
 */
add_action(
	'wp_head',
	function () {
		?>
		<style id="bibletrek-site-tweaks-css">
		/* Fallback: hide any visible author vcard + trailing pipe in Avada meta bars */
		.fusion-meta-info-wrapper:has(> .vcard:not(.rich-snippet-hidden)),
		.fusion-meta-info .fusion-alignleft:has(> .vcard:not(.rich-snippet-hidden)) {
			font-size: 0 !important;
		}
		.fusion-meta-info .vcard,
		.fusion-meta-info .vcard:not(.rich-snippet-hidden) + .fusion-inline-sep {
			display: none !important;
		}
		.fusion-meta-info-wrapper > span:not(.vcard):not(.rich-snippet-hidden),
		.fusion-meta-info-wrapper > a,
		.fusion-meta-info .fusion-alignleft > span:not(.vcard):not(.rich-snippet-hidden),
		.fusion-meta-info .fusion-alignleft > a {
			font-size: var(--meta_font_size, 14px) !important;
		}

		/* Left-align comment form cookie & Jetpack email notification checkboxes */
		#respond p.comment-form-cookies-consent,
		#respond p.comment-subscription-form {
			display: flex !important;
			align-items: center !important;
			justify-content: flex-start !important;
			gap: 10px !important;
			margin: 0 0 10px 0 !important;
			padding: 0 !important;
			text-align: left !important;
			width: 100% !important;
		}
		#respond p.comment-form-cookies-consent input[type="checkbox"],
		#respond p.comment-subscription-form input[type="checkbox"] {
			width: 16px !important;
			height: 16px !important;
			min-width: 16px !important;
			max-width: 16px !important;
			margin: 0 !important;
			padding: 0 !important;
			flex: 0 0 16px !important;
			float: none !important;
		}
		#respond p.comment-form-cookies-consent label,
		#respond p.comment-subscription-form label {
			width: auto !important;
			min-width: 0 !important;
			margin: 0 !important;
			padding: 0 !important;
			flex: 0 1 auto !important;
			float: none !important;
			display: inline-block !important;
			text-align: left !important;
			line-height: 1.45 !important;
			cursor: pointer;
		}
		</style>
		<?php
	},
	999
);
