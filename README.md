# OLX Scraper

Scraper built to automatically collect and store OLX listings 
across multiple categories instead of checking them manually every day.

## Why I built this
I wanted to track prices in categories I follow on OLX.
Doing it manually was annoying so I automated it.

## Technologies
- Python 3.11
- BeautifulSoup4
- Requests
- SQLite
- Pandas

## How to run

1. Install dependencies
pip install -r requirements.txt

2. Run the scraper
python main.py

## Example output

| title | price (PLN) | location | category |
|-------|-------------|----------|----------|
| iPhone 12 Pro 256GB Gold NOWA ORG BATERIA | 1000 | Zabrze | elektronika |
| Komputer gamingowy i7-12700 / RTX 3060 12GB | 4300 | Lodz | elektronika |
| Apple iMac 2025 jak nowy | 5500 | Warszawa | elektronika |
| Dell Latitude 5420 i5 16GB 256GB Win11 | 1099 | Warszawa | elektronika |

Last run: 208 listings across 2 categories (18.06.2026)

## Output files
- olx_data.db - SQLite database with all listings
- olx_data.csv - CSV export

## Known issues
- Selectors may break if OLX changes their HTML layout
- Some listings show NULL price (e.g. barter offers like "Zamienie")

## TODO
- [ ] Add price change tracking over time
- [ ] Schedule automatic daily runs
- [ ] Add more categories (nieruchomosci, motoryzacja)
- [ ] Send email alert when price drops
