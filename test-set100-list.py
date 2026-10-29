import urllib.request
import re

url = "https://www.set.or.th/th/market/information/securities-list/constituents-list-set50-set100"

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

try:
    with urllib.request.urlopen(req, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")
        print("HTTP Status:", response.status)
        print("ขนาดหน้าเว็บ:", len(html), "ตัวอักษร")

        for word in ["SET100", "ADVANC", "AOT", "symbol"]:
            print(word, "พบ", len(re.findall(word, html, re.I)), "ครั้ง")

except Exception as e:
    print("เกิดข้อผิดพลาด:", e)
