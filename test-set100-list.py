
import urllib.request
import re

url = "https://www.set.or.th/en/market/index/set100/overview"

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

# ค้นหารายชื่อหุ้นที่ฝังอยู่ในหน้าเว็บ
symbols = sorted(set(re.findall(
    r'<td[^>]*>\s*([A-Z][A-Z0-9&.-]{1,9})\s*</td>',
    html
)))

print("พบสัญลักษณ์หุ้น:", len(symbols))
print("รายชื่อ:", symbols)
