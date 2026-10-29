import urllib.request
import re
from urllib.parse import urljoin

page = "https://www.set.or.th/th/market/information/securities-list/constituents-list-set50-set100"
req = urllib.request.Request(
    page, headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as r:
    html = r.read().decode("utf-8", errors="replace")

scripts = re.findall(
    r'<script[^>]+src=["\']([^"\']+)',
    html,
    re.I
)

print("พบไฟล์ JavaScript", len(scripts), "ไฟล์")

for src in scripts:
    if "_nuxt/" in src:
        print(urljoin(page, src))
