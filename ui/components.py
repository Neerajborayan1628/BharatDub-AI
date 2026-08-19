"""
Static HTML fragments + small formatting helpers for the BharatDub AI UI.

Nothing in this file touches the dubbing pipeline. Functions here only ever
receive plain strings/bools/numbers that the app already produced and return
HTML strings to render.
"""

import html


# ---------------------------------------------------------------------------
# Header / nav
# ---------------------------------------------------------------------------
NAV_HTML = """
<div class="bd-nav">
  <a href="#bd-workspace">Dubbing</a>
  <a href="#bd-how-it-works">How It Works</a>
  <a href="#bd-languages">Supported Languages</a>
  <a href="#bd-tech">About</a>
  <a class="bd-github" href="https://github.com" target="_blank" rel="noopener">
    ★ GitHub
  </a>
</div>
"""

BRAND_HTML = """
<div class="bd-brand"><span class="bd-brand-name">BharatDub AI</span></div>
"""

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
HERO_HTML = """
<div id="bd-hero">
  <div class="bd-badge">🇮🇳 Hindi-first AI Video Dubbing</div>
  <div class="bd-hero-title">Give your videos a <span>voice</span><br/>in any language.</div>
  <div class="bd-hero-desc">
    Translate, voice-clone and synchronize your videos with AI while preserving the
    original speaker's voice and background sound.
  </div>
  <div class="bd-cap-row">
    <span><b>✓</b> Voice Cloning</span>
    <span><b>✓</b> 15+ Languages</span>
    <span><b>✓</b> Speaker Detection</span>
    <span><b>✓</b> Optional Lip Sync</span>
    <span><b>✓</b> Background Sound Preservation</span>
  </div>
</div>
"""

# ---------------------------------------------------------------------------
# Section headings
# ---------------------------------------------------------------------------
def section_heading(eyebrow: str, title: str) -> str:
    return f"""
<div class="bd-section">
  <div class="bd-section-eyebrow">{html.escape(eyebrow)}</div>
  <div class="bd-section-title">{html.escape(title)}</div>
</div>
"""


def step_head(number: str, title: str, subtitle: str) -> str:
    return f"""
<div class="bd-step-head">
  <div class="bd-step-num">{html.escape(number)}</div>
  <div class="bd-step-title">{html.escape(title)}</div>
</div>
<div class="bd-step-sub">{html.escape(subtitle)}</div>
"""


AUTO_BADGES_HTML = """
<div class="bd-auto-badges">
  <span class="bd-auto-badge">🗣️ Voice: <b>Original speaker (auto-cloned)</b></span>
  <span class="bd-auto-badge">🎭 Emotion: <b>Preserved automatically</b></span>
</div>
"""

# ---------------------------------------------------------------------------
# Feature cards
# ---------------------------------------------------------------------------
FEATURES = [
    ("🎙️", "Voice Cloning", "Preserve the original speaker's vocal identity."),
    ("🌍", "Multilingual", "Dub your videos across multiple languages."),
    ("🎭", "Emotion", "Preserve expressive characteristics where supported."),
    ("👥", "Speaker Detection", "Automatically identify different speakers."),
    ("👄", "Lip Sync", "Synchronize mouth movement with generated speech."),
    ("🔊", "Background Audio", "Keep music and ambient sound in your videos."),
]


def feature_cards_html() -> str:
    cards = "".join(
        f"""
        <div class="bd-feature-card">
          <div class="bd-feature-icon">{icon}</div>
          <div class="bd-feature-title">{html.escape(title)}</div>
          <div class="bd-feature-desc">{html.escape(desc)}</div>
        </div>
        """
        for icon, title, desc in FEATURES
    )
    return f'<div class="bd-feature-grid">{cards}</div>'


# ---------------------------------------------------------------------------
# How it works
# ---------------------------------------------------------------------------
HOW_IT_WORKS = [
    ("01", "Upload", "Upload a video or provide a YouTube URL."),
    ("02", "Analyze", "Detect speakers and transcribe speech."),
    ("03", "Translate", "Translate dialogue into your selected language."),
    ("04", "Generate", "Clone voices and synthesize the new dialogue."),
    ("05", "Deliver", "Synchronize everything into the final dubbed video."),
]


def how_it_works_html() -> str:
    cards = "".join(
        f"""
        <div class="bd-hiw-card">
          <div class="bd-hiw-num">{num}</div>
          <div class="bd-hiw-title">{html.escape(title)}</div>
          <div class="bd-hiw-desc">{html.escape(desc)}</div>
        </div>
        """
        for num, title, desc in HOW_IT_WORKS
    )
    return f'<div id="bd-how-it-works" class="bd-steps-grid">{cards}</div>'


# ---------------------------------------------------------------------------
# Tech stack
# ---------------------------------------------------------------------------
TECH_STACK = ["Whisper", "pyannote.audio", "XTTS", "SpeechBrain", "MarianMT", "Wav2Lip", "FFmpeg"]


def tech_stack_html() -> str:
    chips = "".join(f'<span class="bd-tech-chip">{html.escape(t)}</span>' for t in TECH_STACK)
    return f'<div id="bd-tech" class="bd-tech-chips">{chips}</div>'


RESPONSIBLE_USE_HTML = """
<div class="bd-notice">
  BharatDub AI can clone voices and modify video. Use voice cloning only with appropriate
  permission and respect copyright, privacy and applicable laws.
</div>
"""

FOOTER_HTML = """
<div id="bd-footer">
  <div class="bd-footer-grid">
    <div>
      <div style="color:var(--bd-text); font-weight:700; margin-bottom:4px;">BharatDub AI</div>
      <div>AI-powered multilingual video dubbing.</div>
    </div>
    <div class="bd-footer-links">
      <a href="https://github.com" target="_blank" rel="noopener">GitHub</a>
      <a href="#bd-tech">Documentation</a>
      <a href="#bd-languages">Language Support</a>
    </div>
  </div>
  <div class="bd-footer-copy">See LICENSE in the project repository for license information.</div>
</div>
"""

# ---------------------------------------------------------------------------
# Status panel (idle / processing / success / error)
# ---------------------------------------------------------------------------
PIPELINE_STAGES_HINT = (
    "Extracting audio → detecting speakers → transcribing → translating → "
    "generating voices → synchronizing → finalizing"
)


def idle_status_html() -> str:
    return f"""
<div class="bd-status bd-idle">
  <div class="bd-status-row">
    <span>💤</span>
    <div>
      <div class="bd-status-title">Ready when you are</div>
      <div class="bd-status-sub">Upload a video, choose your languages, and press Start Dubbing.</div>
    </div>
  </div>
</div>
"""


def processing_status_html() -> str:
    return f"""
<div class="bd-status bd-processing">
  <div class="bd-status-row">
    <div class="bd-spinner"></div>
    <div>
      <div class="bd-status-title">Processing your video…</div>
      <div class="bd-status-sub">{html.escape(PIPELINE_STAGES_HINT)}. This can take several
      minutes depending on video length and your chosen settings.</div>
    </div>
  </div>
</div>
"""


def success_status_html(elapsed_seconds: float | None = None) -> str:
    time_str = ""
    if elapsed_seconds is not None:
        time_str = f" in {elapsed_seconds:0.0f}s"
    return f"""
<div class="bd-status bd-success">
  <div class="bd-status-row">
    <span>✅</span>
    <div>
      <div class="bd-status-title">Your dubbed video is ready 🎉</div>
      <div class="bd-status-sub">Finished{html.escape(time_str)}. Preview it below or download it.</div>
    </div>
  </div>
</div>
"""


def _friendly_error_message(raw_message: str) -> str:
    msg = (raw_message or "").lower()
    if "please upload a video" in msg:
        return "Please upload a video or enter a YouTube URL."
    if "hf_token" in msg or "auth" in msg or "unauthorized" in msg or "401" in msg:
        return "Your Hugging Face configuration needs attention."
    if "language" in msg:
        return "This language is not currently supported by the selected model."
    return "Unable to process this video. Check the video format and try again."


def error_status_html(raw_message: str) -> str:
    friendly = _friendly_error_message(raw_message)
    return f"""
<div class="bd-status bd-error">
  <div class="bd-status-row">
    <span>❌</span>
    <div>
      <div class="bd-status-title">Something went wrong</div>
      <div class="bd-status-sub">{html.escape(friendly)}</div>
    </div>
  </div>
</div>
"""


# ---------------------------------------------------------------------------
# Result metadata
# ---------------------------------------------------------------------------
LANGUAGE_FLAGS = {
    "English": "🇬🇧",
    "Spanish": "🇪🇸",
    "French": "🇫🇷",
    "German": "🇩🇪",
    "Italian": "🇮🇹",
    "Turkish": "🇹🇷",
    "Russian": "🇷🇺",
    "Dutch": "🇳🇱",
    "Czech": "🇨🇿",
    "Arabic": "🇸🇦",
    "Chinese (Simplified)": "🇨🇳",
    "Japanese": "🇯🇵",
    "Korean": "🇰🇷",
    "Hindi": "🇮🇳",
    "Hungarian": "🇭🇺",
}


def lang_label(name: str) -> str:
    flag = LANGUAGE_FLAGS.get(name, "")
    return f"{flag} {name}".strip()


def result_metadata_html(source_language, target_language, use_wav2lip, bg_sound, elapsed_seconds=None) -> str:
    time_str = f"{elapsed_seconds:0.0f}s" if elapsed_seconds is not None else "—"
    items = [
        ("Source", lang_label(source_language)),
        ("Target", lang_label(target_language)),
        ("Voice", "Original speaker"),
        ("Lip Sync", "Enabled" if use_wav2lip else "Disabled"),
        ("Background Sound", "Enabled" if bg_sound else "Disabled"),
        ("Processing time", time_str),
    ]
    grid = "".join(
        f"""
        <div class="bd-meta-item">
          <div class="bd-meta-label">{html.escape(label)}</div>
          <div class="bd-meta-value">{html.escape(str(value))}</div>
        </div>
        """
        for label, value in items
    )
    return f'<div class="bd-meta-grid">{grid}</div>'
