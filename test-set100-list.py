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

for name in files:
    url = "https://www.set.or.th/_nuxt/" + name
    req = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0"}
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            js = r.read().decode("utf-8", errors="replace")

        hits = []
        for pattern in [
            r"constituents",
            r"set50-set100",
            r"api/[^\"']{0,120}",
            r"\$get\([^)]{0,200}"
        ]:
            for m in list(re.finditer(pattern, js, re.I))[:3]:
                hits.append(m.group(0))

        if hits:
            print("\n###", name, "###")
            for hit in hits:
                print(hit[:250])

    except Exception as e:
        print(name, "ERROR:", e)
