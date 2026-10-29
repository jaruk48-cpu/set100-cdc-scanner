import urllib.request
import re

files = [
    "ec7dc67.js", "bdbbc32.js", "83eb973.js",
    "365b61e.js", "12921c6.js", "02ed788.js",
    "128a4f2.js", "2742534.js", "e67f5f1.js",
    "4ed2d59.js", "62c1857.js", "ed89921.js",
    "f32c284.js", "0abceb1.js", "c1873ec.js",
    "c1939f8.js"
]

terms = [
    "constituents-list",
    "constituentsList",
    "securities-list",
    "getIndexCompositionList",
    "api/set/index"
]

for name in files:
    req = urllib.request.Request(
        "https://www.set.or.th/_nuxt/" + name,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            js = r.read().decode("utf-8", errors="replace")

        printed = False
        for term in terms:
            matches = list(re.finditer(re.escape(term), js, re.I))
            if matches:
                if not printed:
                    print("\n###", name, "###")
                    printed = True
                print(term, "พบ", len(matches), "ครั้ง")
                for m in matches[:2]:
                    print(js[max(0, m.start()-250):m.end()+500])
                    print("---")

    except Exception as e:
        print(name, "ERROR:", e)
