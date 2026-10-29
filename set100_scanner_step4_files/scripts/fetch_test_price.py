import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Infrastructure test only: Yahoo Finance symbol for Advanced Info Service.
symbol = "ADVANC.BK"
url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=3mo&interval=1d"
request = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0 SET100-CDC-Scanner prototype"}
)
with urllib.request.urlopen(request, timeout=30) as response:
    payload = json.loads(response.read().decode("utf-8"))

result = payload.get("chart", {}).get("result")
if not result:
    error = payload.get("chart", {}).get("error")
    raise RuntimeError(f"No price data returned for {symbol}: {error}")

chart = result[0]
timestamps = chart.get("timestamp") or []
quotes = chart.get("indicators", {}).get("quote", [{}])[0]
closes = quotes.get("close") or []
rows = []
for ts, close in zip(timestamps, closes):
    if close is None:
        continue
    date = datetime.fromtimestamp(ts, timezone.utc).date().isoformat()
    rows.append({"date": date, "close": round(float(close), 4)})

if len(rows) < 27:
    raise RuntimeError(f"Too few daily closes returned: {len(rows)}")

output = {
    "source": "Yahoo Finance chart endpoint (unofficial; test only)",
    "symbol": symbol,
    "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
    "rows": rows
}
path = Path("data/test-price.json")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {len(rows)} daily closes to {path}")
