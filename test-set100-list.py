import urllib.request
import re

url = "https://www.set.or.th/en/market/index/set100/overview"
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

try:
    with urllib.request.urlopen(req, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")

    print("ขนาดหน้าเว็บ:", len(html), "ตัวอักษร")
    print("พบคำว่า ADVANC:", "ADVANC" in html)
    print("พบคำว่า Constituents:", "Constituents" in html)

    symbols = sorted(set(re.findall(
        r'"symbol"\s*:\s*"([A-Z0-9]{2,10})"',
        html
    )))

    print("จำนวน Symbol ที่พบ:", len(symbols))
    print("ตัวอย่าง:", symbols[:20])

except Exception as e:
    print("เกิดข้อผิดพลาด:", repr(e))
    raise
