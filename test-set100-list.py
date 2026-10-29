import urllib.request
import re

URL = "https://www.set.or.th/en/market/index/set100/overview"

req = urllib.request.Request(
    URL, headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

print("ความยาว HTML:", len(html))
print("ตารางที่พบในหน้าเว็บ:")

tables = re.findall(r'<table\b[^>]*>', html, re.IGNORECASE)
for table in tables:
    print(table)

print("\nตัวอย่างบริเวณที่มี ADVANC:")
match = re.search("ADVANC", html, re.IGNORECASE)
if match:
    print(html[max(0, match.start()-200):match.end()+300])
else:
    print("ไม่พบ ADVANC ใน HTML")
