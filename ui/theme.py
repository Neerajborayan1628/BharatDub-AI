"""
Visual theme for BharatDub AI.

This module only builds a `gr.Theme` and a CSS string. It never imports
anything from the dubbing pipeline, so it can't affect functionality.

Design tokens (also mirrored as CSS variables in CUSTOM_CSS so the theme
is easy to re-skin later):

    --bg             page background
    --surface        card / panel background
    --surface-hover  hovered / alt surface
    --text           primary text
    --text-muted     secondary text
    --border         hairline borders
    --accent         brand accent (saffron, nodding to the Indian flag)
    --accent-hover   accent hover state
"""

import gradio as gr

# ---------------------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------------------
BG = "#0b0d10"
SURFACE = "#14171c"
SURFACE_HOVER = "#1b1f26"
BORDER = "#252932"
TEXT = "#f4f5f7"
TEXT_MUTED = "#98a1ac"
ACCENT = "#ff7a45"
ACCENT_HOVER = "#ff9163"
ACCENT_SOFT = "rgba(255, 122, 69, 0.14)"
SUCCESS = "#3ecf8e"
ERROR = "#ff6b6b"


def _build_theme() -> gr.Theme:
    """Build the Gradio theme defensively.

    Gradio's theme-builder keyword surface has shifted a little between
    versions. If any kwarg here isn't recognized by the installed Gradio
    version, we fall back to a bare Base() theme rather than crashing the
    whole app -- the custom CSS below still carries almost all of the
    visual design on its own.
    """
    try:
        return gr.themes.Base(
            primary_hue=gr.themes.colors.orange,
            neutral_hue=gr.themes.colors.slate,
            font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"],
            font_mono=[gr.themes.GoogleFont("JetBrains Mono"), "ui-monospace", "monospace"],
        ).set(
            body_background_fill=BG,
            body_background_fill_dark=BG,
            background_fill_primary=SURFACE,
            background_fill_primary_dark=SURFACE,
            background_fill_secondary=SURFACE_HOVER,
            background_fill_secondary_dark=SURFACE_HOVER,
            border_color_primary=BORDER,
            border_color_primary_dark=BORDER,
            block_background_fill=SURFACE,
            block_background_fill_dark=SURFACE,
            block_border_color=BORDER,
            block_border_color_dark=BORDER,
            block_label_text_color=TEXT_MUTED,
            block_label_text_color_dark=TEXT_MUTED,
            block_title_text_color=TEXT,
            block_title_text_color_dark=TEXT,
            body_text_color=TEXT,
            body_text_color_dark=TEXT,
            body_text_color_subdued=TEXT_MUTED,
            body_text_color_subdued_dark=TEXT_MUTED,
            button_primary_background_fill=ACCENT,
            button_primary_background_fill_dark=ACCENT,
            button_primary_background_fill_hover=ACCENT_HOVER,
            button_primary_background_fill_hover_dark=ACCENT_HOVER,
            button_primary_text_color="#1a0e08",
            button_primary_text_color_dark="#1a0e08",
            button_secondary_background_fill=SURFACE_HOVER,
            button_secondary_background_fill_dark=SURFACE_HOVER,
            button_secondary_border_color=BORDER,
            button_secondary_border_color_dark=BORDER,
            button_secondary_text_color=TEXT,
            button_secondary_text_color_dark=TEXT,
            input_background_fill=SURFACE_HOVER,
            input_background_fill_dark=SURFACE_HOVER,
            input_border_color=BORDER,
            input_border_color_dark=BORDER,
            checkbox_background_color=SURFACE_HOVER,
            checkbox_background_color_dark=SURFACE_HOVER,
            checkbox_background_color_selected=ACCENT,
            checkbox_background_color_selected_dark=ACCENT,
            shadow_drop="0 1px 2px rgba(0,0,0,0.35)",
        )
    except Exception:
        return gr.themes.Base()


THEME = _build_theme()

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CUSTOM_CSS = f"""
:root {{
    --bd-bg: {BG};
    --bd-surface: {SURFACE};
    --bd-surface-hover: {SURFACE_HOVER};
    --bd-border: {BORDER};
    --bd-text: {TEXT};
    --bd-text-muted: {TEXT_MUTED};
    --bd-accent: {ACCENT};
    --bd-accent-hover: {ACCENT_HOVER};
    --bd-accent-soft: {ACCENT_SOFT};
    --bd-success: {SUCCESS};
    --bd-error: {ERROR};
}}

/* ---------- base page ---------- */
.gradio-container {{
    background: var(--bd-bg) !important;
    color: var(--bd-text) !important;
    max-width: 1180px !important;
}}
body {{ background: var(--bd-bg) !important; }}
.gradio-container * {{ box-sizing: border-box; }}
footer {{ display: none !important; }}

/* ---------- header ---------- */
#bd-header {{
    align-items: center !important;
    padding: 14px 4px 18px 4px;
    border-bottom: 1px solid var(--bd-border);
    margin-bottom: 8px;
    gap: 8px;
}}
#bd-logo-img img {{
    border-radius: 8px;
    object-fit: contain;
}}
#bd-logo-img {{
    width: 40px !important;
    min-width: 40px !important;
    flex-grow: 0 !important;
    box-shadow: none !important;
    background: transparent !important;
    border: none !important;
}}
#bd-logo-img .image-container {{ background: transparent !important; border: none !important; }}
.bd-brand {{
    display: flex; align-items: center; gap: 10px;
}}
.bd-brand-name {{
    font-size: 18px; font-weight: 700; letter-spacing: -0.01em; color: var(--bd-text);
}}
.bd-nav {{
    display: flex; align-items: center; justify-content: flex-end; gap: 26px;
    flex-wrap: wrap;
}}
.bd-nav a {{
    color: var(--bd-text-muted); text-decoration: none; font-size: 14px; font-weight: 500;
    transition: color .15s ease;
}}
.bd-nav a:hover {{ color: var(--bd-text); }}
.bd-nav .bd-github {{
    display: inline-flex; align-items: center; gap: 6px;
    padding: 7px 14px; border: 1px solid var(--bd-border); border-radius: 8px;
    color: var(--bd-text) !important;
}}
.bd-nav .bd-github:hover {{ background: var(--bd-surface-hover); }}

/* ---------- hero ---------- */
#bd-hero {{ padding: 42px 8px 8px 8px; text-align: center; }}
.bd-badge {{
    display: inline-flex; align-items: center; gap: 6px;
    background: var(--bd-accent-soft); color: var(--bd-accent);
    border: 1px solid rgba(255,122,69,0.3);
    padding: 6px 14px; border-radius: 999px; font-size: 13px; font-weight: 600;
    margin-bottom: 22px;
}}
.bd-hero-title {{
    font-size: 46px; line-height: 1.12; font-weight: 800; letter-spacing: -0.02em;
    margin: 0 0 14px 0; color: var(--bd-text);
}}
.bd-hero-title span {{ color: var(--bd-accent); }}
.bd-hero-desc {{
    max-width: 620px; margin: 0 auto 30px auto; color: var(--bd-text-muted);
    font-size: 16.5px; line-height: 1.6;
}}
.bd-hero-ctas {{ display: flex; gap: 14px; justify-content: center; margin-bottom: 34px; flex-wrap: wrap; }}
.bd-cap-row {{
    display: flex; flex-wrap: wrap; justify-content: center; gap: 10px 22px;
    color: var(--bd-text-muted); font-size: 13.5px; margin-bottom: 8px;
}}
.bd-cap-row span {{ display: inline-flex; align-items: center; gap: 6px; }}
.bd-cap-row b {{ color: var(--bd-success); font-weight: 700; }}

/* ---------- generic section heading ---------- */
.bd-section {{ padding: 54px 6px 6px 6px; }}
.bd-section-eyebrow {{
    color: var(--bd-accent); font-size: 13px; font-weight: 700; letter-spacing: .06em;
    text-transform: uppercase; text-align: center; margin-bottom: 10px;
}}
.bd-section-title {{
    font-size: 28px; font-weight: 800; text-align: center; color: var(--bd-text);
    letter-spacing: -0.01em; margin-bottom: 40px;
}}

/* ---------- workspace step cards ---------- */
.bd-step-card {{
    background: var(--bd-surface) !important;
    border: 1px solid var(--bd-border) !important;
    border-radius: 16px !important;
    padding: 22px 22px 8px 22px !important;
    margin-bottom: 18px !important;
}}
.bd-step-head {{
    display: flex; align-items: center; gap: 10px; margin-bottom: 4px;
}}
.bd-step-num {{
    width: 24px; height: 24px; border-radius: 7px; background: var(--bd-accent-soft);
    color: var(--bd-accent); font-size: 12.5px; font-weight: 800;
    display: flex; align-items: center; justify-content: center; flex: none;
}}
.bd-step-title {{ font-size: 15px; font-weight: 700; color: var(--bd-text); }}
.bd-step-sub {{ color: var(--bd-text-muted); font-size: 13px; margin: 2px 0 14px 34px; }}
.bd-hint {{ color: var(--bd-text-muted); font-size: 12.5px; margin-top: -6px; }}

.bd-auto-badges {{ display: flex; gap: 10px; flex-wrap: wrap; margin: 4px 0 14px 0; }}
.bd-auto-badge {{
    display: inline-flex; align-items: center; gap: 6px;
    background: var(--bd-surface-hover); border: 1px solid var(--bd-border);
    color: var(--bd-text-muted); border-radius: 999px; padding: 6px 12px; font-size: 12.5px;
}}
.bd-auto-badge b {{ color: var(--bd-text); font-weight: 600; }}

#bd-swap-btn {{
    min-width: 40px !important; max-width: 44px !important; height: 40px !important;
    border-radius: 10px !important; align-self: flex-end;
}}

/* ---------- primary CTA ---------- */
#bd-submit {{
    font-size: 16px !important; font-weight: 700 !important; padding: 16px !important;
    border-radius: 12px !important; box-shadow: 0 8px 24px rgba(255,122,69,0.22) !important;
}}

/* ---------- status / processing panel ---------- */
.bd-status {{
    border-radius: 14px; border: 1px solid var(--bd-border); background: var(--bd-surface);
    padding: 16px 18px; margin-top: 4px; font-size: 14px;
}}
.bd-status.bd-idle {{ color: var(--bd-text-muted); }}
.bd-status.bd-processing {{ border-color: rgba(255,122,69,0.4); color: var(--bd-text); }}
.bd-status.bd-success {{ border-color: rgba(62,207,142,0.4); color: var(--bd-text); }}
.bd-status.bd-error {{ border-color: rgba(255,107,107,0.4); color: var(--bd-text); }}
.bd-status-row {{ display: flex; align-items: center; gap: 10px; }}
.bd-spinner {{
    width: 16px; height: 16px; border-radius: 50%;
    border: 2px solid var(--bd-border); border-top-color: var(--bd-accent);
    animation: bd-spin 0.8s linear infinite; flex: none;
}}
@keyframes bd-spin {{ to {{ transform: rotate(360deg); }} }}
.bd-status-title {{ font-weight: 700; }}
.bd-status-sub {{ color: var(--bd-text-muted); font-size: 13px; margin-top: 4px; }}

/* ---------- result metadata ---------- */
.bd-meta-grid {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 10px; margin-top: 12px;
}}
.bd-meta-item {{
    background: var(--bd-surface-hover); border: 1px solid var(--bd-border); border-radius: 12px;
    padding: 10px 12px;
}}
.bd-meta-label {{ color: var(--bd-text-muted); font-size: 11.5px; text-transform: uppercase; letter-spacing: .04em; }}
.bd-meta-value {{ color: var(--bd-text); font-size: 14px; font-weight: 700; margin-top: 2px; }}

/* ---------- feature cards ---------- */
.bd-feature-grid {{
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;
}}
.bd-feature-card {{
    background: var(--bd-surface); border: 1px solid var(--bd-border); border-radius: 16px;
    padding: 22px; transition: border-color .15s ease, transform .15s ease;
}}
.bd-feature-card:hover {{ border-color: var(--bd-accent); transform: translateY(-2px); }}
.bd-feature-icon {{ font-size: 22px; margin-bottom: 12px; }}
.bd-feature-title {{ font-size: 15px; font-weight: 700; color: var(--bd-text); margin-bottom: 6px; }}
.bd-feature-desc {{ font-size: 13.5px; color: var(--bd-text-muted); line-height: 1.55; }}

/* ---------- how it works ---------- */
.bd-steps-grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; }}
.bd-hiw-card {{
    background: var(--bd-surface); border: 1px solid var(--bd-border); border-radius: 14px;
    padding: 18px 16px;
}}
.bd-hiw-num {{ color: var(--bd-accent); font-weight: 800; font-size: 13px; margin-bottom: 10px; }}
.bd-hiw-title {{ font-weight: 700; font-size: 14px; color: var(--bd-text); margin-bottom: 6px; }}
.bd-hiw-desc {{ font-size: 12.5px; color: var(--bd-text-muted); line-height: 1.5; }}

/* ---------- tech chips ---------- */
.bd-tech-chips {{ display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; }}
.bd-tech-chip {{
    border: 1px solid var(--bd-border); background: var(--bd-surface); color: var(--bd-text-muted);
    padding: 8px 16px; border-radius: 999px; font-size: 13px; font-weight: 600;
}}

/* ---------- responsible use ---------- */
.bd-notice {{
    text-align: center; color: var(--bd-text-muted); font-size: 12.5px; line-height: 1.6;
    max-width: 720px; margin: 34px auto 0 auto; padding: 14px 18px;
    border: 1px dashed var(--bd-border); border-radius: 12px;
}}

/* ---------- footer ---------- */
#bd-footer {{
    margin-top: 54px; padding: 28px 6px 10px 6px; border-top: 1px solid var(--bd-border);
    color: var(--bd-text-muted); font-size: 13px;
}}
.bd-footer-grid {{ display: flex; justify-content: space-between; flex-wrap: wrap; gap: 16px; }}
.bd-footer-links a {{ color: var(--bd-text-muted); text-decoration: none; margin-left: 18px; }}
.bd-footer-links a:hover {{ color: var(--bd-text); }}
.bd-footer-copy {{ margin-top: 16px; font-size: 12px; opacity: .7; }}

/* ---------- misc component polish ---------- */
.bd-video video {{ border-radius: 14px !important; }}
#bd-upload-hint {{ text-align: center; color: var(--bd-text-muted); font-size: 12px; margin-top: -4px; }}

/* ---------- responsive ---------- */
@media (max-width: 900px) {{
    .bd-hero-title {{ font-size: 32px; }}
    .bd-feature-grid {{ grid-template-columns: 1fr; }}
    .bd-steps-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .bd-nav {{ justify-content: center; }}
    #bd-header {{ flex-direction: column; }}
}}
"""
