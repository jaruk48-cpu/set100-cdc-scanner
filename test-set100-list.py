import urllib.request

url = "https://www.set.or.th/api/set/index/set100/composition?lang=en"

req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": "https://www.set.or.th/en/market/index/set100/overview",
        "Origin": "https://www.set.or.th"
    }
)

try:
    with urllib.request.urlopen(req, timeout=30) as response:
        data = response.read().decode("utf-8", errors="replace")
        print("HTTP Status:", response.status)
        print("Response:")
        print(data[:3000])
except Exception as e:
    print("API ERROR:", e)
