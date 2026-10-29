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

    print("HTTP Status: 200")
    print("Page length:", len(html))

    symbols = re.findall(
        r'<tr[^>]*>.*?<td[^>]*>\s*([A-Z0-9&.-]+)\s*</td>',
        html,
        re.I | re.S
    )

    print("Symbols found:", len(symbols))
    print("First symbols:", symbols[:20])

except Exception as e:
    print("PAGE ERROR:", e)
