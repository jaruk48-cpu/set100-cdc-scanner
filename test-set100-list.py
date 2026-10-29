import urllib.request
import re

url = "https://www.set.or.th/th/market/information/securities-list/constituents-list-set50-set100"
req = urllib.request.Request(
    url, headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

for word in ["SET100", "ADVANC", "PTT", "AOT", "constituents"]:
    print("\n###", word, "###")
    matches = list(re.finditer(word, html, re.I))
    print("พบ", len(matches), "ตำแหน่ง")
    for m in matches[:2]:
        start = max(0, m.start() - 250)
        end = min(len(html), m.end() + 400)
        print(re.sub(r"\s+", " ", html[start:end]))
