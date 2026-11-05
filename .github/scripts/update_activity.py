from datetime import datetime, timezone
from html import escape
from pathlib import Path
import os

actor = os.environ["ACTOR"]
sha = os.environ["SOURCE_SHA"]
stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
page = Path("index.html")
html = page.read_text(encoding="utf-8")
entry = f"<p>Updated by {escape(actor)} on {stamp} [Commit: {sha}]</p>"
if "</body>" in html:
    html = html.replace("</body>", entry + "\n</body>", 1)
else:
    # The original practical page is an HTML fragment, without a closing body tag.
    html = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>UTS Git Practice</title></head><body>\n' + html + entry + '\n</body></html>\n'
page.write_text(html, encoding="utf-8")
with Path("README.md").open("a", encoding="utf-8") as readme:
    readme.write(f"\n### Updated by {actor} on {stamp} [Commit: {sha}]\n")
