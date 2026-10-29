import urllib.request
import re

BASE = "https://www.set.or.th"
SCRIPTS = [
    "/_nuxt/ec7dc67.js",
    "/_nuxt/b3a07d8.js",
    "/_nuxt/83eb973.js",
    "/_nuxt/56696a5.js",
    "/_nuxt/7777eae.js",
    "/_nuxt/365b61e.js",
    "/_nuxt/0abceb1.js",
    "/_nuxt/c1873ec.js",
    "/_nuxt/c1939f8.js",
]

KEYWORDS = [
    "constituents",
    "market-index-overview",
    "api/",
    "set100",
    "indexComposition",
]

for path in SCRIPTS:
    url = BASE + path
    print("\n---", path, "---")

    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            js = response.read().decode("utf-8", errors="replace")

        found = False
        for word in KEYWORDS:
            for match in list(re.finditer(word, js, re.I))[:3]:
                start = max(0, match.start() - 120)
                end = min(len(js), match.end() + 220)
                print("คำค้น:", word)
                print(js[start:end])
                found = True

        if not found:
            print("ไม่พบคำค้น")

    except Exception as e:
        print("เกิดข้อผิดพลาด:", e)
