"""Static language-support verification for BharatDub AI.

This script checks that Hindi is wired into the project UI mapping and that
the dubbing pipeline passes the selected target language into XTTS.
It does not download models or run inference.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
app = (root / "app.py").read_text(encoding="utf-8")
inference = (root / "inference.py").read_text(encoding="utf-8")

assert re.search(r"['\"]Hindi['\"]\s*:\s*['\"]hi['\"]", app),     "Hindi is missing from app.py language_mapping."
assert "language=self.target_language" in inference,     "Target language is not passed to XTTS."
assert "BharatDub AI" in app or "BharatDub AI" in inference,     "BharatDub AI branding was not applied."

print("PASS: Hindi is mapped to 'hi' and is passed to XTTS.")
