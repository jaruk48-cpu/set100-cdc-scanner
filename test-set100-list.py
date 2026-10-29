import urllib.request
import re

URL = "https://www.set.or.th/en/market/index/set100/overview"

req = urllib.request.Request(
    URL, headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

scripts = re.findall(
    r'<script[^>]+src=["\']([^"\']+)',
    html,
    re.IGNORECASE
)

print("ไฟล์ JavaScript ที่เกี่ยวข้อง:")
for script in scripts:
    if "_nuxt/" in script:
        print("https://www.set.or.th" + script)

print("\nคำใบ้เกี่ยวกับข้อมูลตาราง:")
for word in ["market-index-overview", "TableOther", "constituents"]:
    print(word, "พบ", len(re.findall(word, html, re.IGNORECASE)), "ครั้ง")
