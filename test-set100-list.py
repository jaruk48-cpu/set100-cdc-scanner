import urllib.request
import json

url = "https://www.set.or.th/api/set/index/set100/composition?lang=en"

req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.set.or.th/en/market/index/set100/overview",
        "Accept": "application/json"
    }
)

try:
    with urllib.request.urlopen(req, timeout=30) as response:
        print("HTTP Status:", response.status)
        data = json.loads(response.read().decode("utf-8"))

    print(json.dumps(data, indent=2, ensure_ascii=False)[:12000])

except Exception as e:
    print("เกิดข้อผิดพลาด:", e)
