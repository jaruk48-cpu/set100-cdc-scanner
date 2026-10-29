import urllib.request
import re

URL = "https://www.set.or.th/en/market/index/set100/overview"

req = urllib.request.Request(
    URL, headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

for phrase in ["table-wimfm6bgm6", "aria-busy", "ADVANC"]:
    print(f"\n--- {phrase} ---")
    matches = list(re.finditer(phrase, html, re.IGNORECASE))
    print("พบ:", len(matches))
    for m in matches[:2]:
        start = max(0, m.start() - 500)
        end = min(len(html), m.end() + 1200)
        print(html[start:end])
