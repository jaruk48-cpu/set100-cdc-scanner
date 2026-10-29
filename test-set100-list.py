import re
import json
import urllib.request
from html.parser import HTMLParser

URL = "https://www.set.or.th/en/market/index/set100/overview"

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_row = False
        self.in_cell = False
        self.cell = ""
        self.row = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.in_row = True
            self.row = []
        elif tag in ("td", "th") and self.in_row:
            self.in_cell = True
            self.cell = ""

    def handle_data(self, data):
        if self.in_cell:
            self.cell += data

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.in_cell:
            self.row.append(self.cell.strip())
            self.in_cell = False
        elif tag == "tr" and self.in_row:
            self.rows.append(self.row)
            self.in_row = False

req = urllib.request.Request(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

try:
    with urllib.request.urlopen(req, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")

    parser = TableParser()
    parser.feed(html)

    symbols = []
    for row in parser.rows:
        if not row:
            continue
        symbol = re.sub(r"\s+", "", row[0]).upper()
        if re.fullmatch(r"[A-Z0-9]{2,10}", symbol):
            if symbol not in ("SYMBOL", "SET100"):
                symbols.append(symbol)

    symbols = sorted(set(symbols))

    print("จำนวนรายชื่อที่อ่านได้:", len(symbols))
    print(json.dumps(symbols, ensure_ascii=False, indent=2))

    if len(symbols) < 80:
        print("คำเตือน: อาจอ่านตารางไม่ได้ครบ เพราะหน้า SET โหลดข้อมูลแบบไดนามิก")
except Exception as e:
    print("ดึงข้อมูลไม่สำเร็จ:", repr(e))
