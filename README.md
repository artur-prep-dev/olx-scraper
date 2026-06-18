# OLX Scraper

Web scraper that collects listings from OLX.pl and stores them in SQLite database.

## Problem
Manually checking OLX listings is time-consuming. 
This scraper automates data collection across multiple categories.

## Technologies
- Python 3.10+
- BeautifulSoup4
- Requests
- SQLite
- Pandas

## How to run

1. Install dependencies
pip install -r requirements.txt

2. Run the scraper
python main.py

## Output
- olx_data.db - SQLite database
- olx_data.csv - CSV export

## Note
For my portfolio