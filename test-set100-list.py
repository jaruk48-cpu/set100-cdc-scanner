import re
import urllib.request
from html import unescape

url = "https://www.set.or.th/en/market/index/set100/overview"
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

print("HTML length:", len(html))

for word in ["api", "constituents", "set100", "ADVANC"]:
    print(f"\n--- {word} ---")
    matches = list(re.finditer(word, html, re.I))
    print("พบ:", len(matches), "ตำแหน่ง")

    for match in matches[:3]:
        start = max(0, match.start() - 180)
        end = min(len(html), match.end() + 300)
        print(unescape(html[start:end]).replace("\n", " ")[:500])

urls = sorted(set(re.findall(
    r'https?[^"\'\s<>]+',
    html
)))

print("\n--- URL ที่น่าสนใจ ---")
for item in urls:
    if any(word in item.lower() for word in ["api", "index", "quote"]):
        print(item[:300])
