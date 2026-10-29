import urllib.request
import re

url = "https://www.set.or.th/_nuxt/b3a07d8.js"
req = urllib.request.Request(
    url, headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    js = response.read().decode("utf-8", errors="replace")

for word in [
    "getIndexCompositionList",
    "compositionList:",
    "compositionList:function",
]:
    print("\n====", word, "====")
    matches = list(re.finditer(re.escape(word), js, re.I))
    print("พบ", len(matches), "ตำแหน่ง")

    for match in matches[:5]:
        start = max(0, match.start() - 500)
        end = min(len(js), match.end() + 1000)
        print(js[start:end])
        print("\n--------------------")
