import re
import urllib.request
from html.parser import HTMLParser

URL = "https://www.set.or.th/en/market/index/set100/overview"

class TableParser(HTMLParser):
    def _init_(self):
        super()._init_()
        self.rows = []
        self.row = None
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.cell = ""
        elif tag == "br" and self.cell is not None:
            self.cell += " "

    def handle_data(self, data):
        if self.cell is not None:
            self.cell += data

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.row is not None:
            self.row.append(" ".join(self.cell.split()))
            self.cell = None
        elif tag == "tr" and self.row is not None:
            if self.row:
                self.rows.append(self.row)
            self.row = None
            self.cell = None

req = urllib.request.Request(
    URL, headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

parser = TableParser()
parser.feed(html)

print("จำนวนแถวในตาราง:", len(parser.rows))
print("\nตัวอย่างแถวแรก:")

for row in parser.rows[:12]:
    print(repr(row))

print("\nแถวที่มี ADVANC:")
for row in parser.rows:
    if any("ADVANC" in cell.upper() for cell in row):
        print(repr(row))
