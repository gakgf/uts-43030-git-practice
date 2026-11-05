#!/usr/bin/env bash
set -euo pipefail
python - "$1" "$2" "${REPORT_PATH:-index.html}" <<'PY'
from pathlib import Path
from html import escape
import re
import sys
tasks = Path(sys.argv[1]).read_text(encoding="utf-8")
tests = Path(sys.argv[2]).read_text(encoding="utf-8")
report = Path(sys.argv[3])
todo, done = tasks.split("ToDo Tasks:\n", 1)[1].split("Done Tasks:\n", 1)
html = report.read_text(encoding="utf-8")
for element, content in (("todo", todo), ("done", done), ("tests", tests)):
    pattern = rf'(<pre id="{element}">).*?(</pre>)'
    html, count = re.subn(pattern, lambda m: m[1] + escape(content.strip()) + m[2], html, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected one report target: {element}")
report.write_text(html, encoding="utf-8")
PY
