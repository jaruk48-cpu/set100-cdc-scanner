import urllib.request
from html.parser import HTMLParser

URL = "https://www.set.or.th/en/market/index/set100/overview"

class TableParser(HTMLParser):
    def _init_(self):
        super()._init_()
        self.in_table = False
        self.in_cell = False
        self.rows = []
        self.row = []
        self.cell = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table" and attrs.get("id") == "table-cfmw03jkzw":
            self.in_table = True
        elif self.in_table and tag == "tr":
            self.row = []
        elif self.in_table and tag in ("td", "th"):
            self.in_cell = True
            self.cell = ""

    def handle_data(self, data):
        if self.in_table and self.in_cell:
            self.cell += data

    def handle_endtag(self, tag):
        if self.in_table and tag in ("td", "th") and self.in_cell:
            self.row.append(" ".join(self.cell.split()))
            self.in_cell = False
        elif self.in_table and tag == "tr":
            if self.row:
                self.rows.append(self.row)
        elif tag == "table" and self.in_table:
            self.in_table = False

req = urllib.request.Request(
    URL, headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="replace")

parser = TableParser()
parser.feed(html)

print("จำนวนแถว:", len(parser.rows))
for row in parser.rows[:15]:
    print(row)
