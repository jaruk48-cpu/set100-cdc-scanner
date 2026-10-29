import urllib.request
import re

scripts = [
    "ec7dc67.js", "b3a07d8.js", "83eb973.js",
    "56696a5.js", "7777eae.js", "365b61e.js",
    "0abceb1.js", "c1873ec.js", "c1939f8.js"
]

for name in scripts:
    url = "https://www.set.or.th/_nuxt/" + name
    req = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0"}
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            js = r.read().decode("utf-8", errors="replace")

        if "getIndexCompositionList" in js or "market/index/getIndexCompositionList" in js:
            print("\n###", name, "###")

            for pattern in [
                r'getIndexCompositionList.{0,500}',
                r'getIndexCompositionList.{0,1000}',
                r'compositionList.{0,300}',
                r'baseURL.{0,200}',
            ]:
                for m in list(re.finditer(pattern, js, re.I))[:2]:
                    print(m.group(0)[:1000])
                    print("---")

    except Exception as e:
        print(name, e)
