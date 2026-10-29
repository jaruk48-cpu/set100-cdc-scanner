import urllib.request
import re

URL = "https://www.set.or.th/en/market/index/set100/overview"

req = urllib.request.Request(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

print("ความยาวหน้าเว็บ:", len(html))

print("\n--- คำที่เกี่ยวข้องกับ SET100 ---")
for word in ["SET100", "constituent", "api", "ADVANC"]:
    matches = list(re.finditer(word, html, re.IGNORECASE))
    print(f"\n{word}: พบ {len(matches)} จุด")
    for match in matches[:3]:
        start = max(0, match.start() - 150)
        end = min(len(html), match.end() + 250)
        print(html[start:end].replace("\n", " "))

print("\n--- ลิงก์ JavaScript ---")
scripts = re.findall(
    r'<script[^>]+src=["\']([^"\']+)',
    html,
    re.IGNORECASE
)
for script in scripts[:20]:
    print(script)
