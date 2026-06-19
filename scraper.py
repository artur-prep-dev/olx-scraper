import requests
from bs4 import BeautifulSoup
import time
import random

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "pl-PL,pl;q=0.9",
}

def get_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"Blad pobierania strony: {e}")
        return None

def scrape_listings(soup, category):
    listings = []

    # OLX oznacza karty ogloszen przez data-cy="l-card"
    cards = soup.find_all("div", attrs={"data-cy": "l-card"})

    if not cards:
        print("Nie znaleziono ogloszen")
        return listings

    for card in cards:
        try:
            title_tag = card.find("h4")
            title = title_tag.text.strip() if title_tag else None

            price_tag = card.find("p", attrs={"data-testid": "ad-price"})
            price = price_tag.text.strip() if price_tag else None

            location_tag = card.find("p", attrs={"data-testid": "location-date"})
            location_date = location_tag.text.strip() if location_tag else ""

            parts = location_date.split(" - ")
            location = parts[0] if parts else ""
            date_added = parts[-1] if len(parts) > 1 else ""

            link_tag = card.find("a")
            url = "https://www.olx.pl" + link_tag["href"] if link_tag else None

            if title and url:
                listings.append({
                    "title": title,
                    "price": price,
                    "location": location,
                    "date_added": date_added,
                    "url": url,
                    "category": category
                })

        except Exception as e:
            print(f"Blad przy parsowaniu: {e}")
            continue

    return listings

def scrape_category(base_url, category, max_pages=3):
    all_listings = []

    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Scrapuje strone {page}: {url}")

        soup = get_page(url)

        if not soup:
            break

        listings = scrape_listings(soup, category)

        if not listings:
            print(f"Brak ogloszen na stronie {page}")
            break

        all_listings.extend(listings)
        print(f"Znaleziono {len(listings)} ogloszen na stronie {page}")

        # losowy delay zeby OLX nas nie zablokowal
        time.sleep(random.uniform(2, 5))

    return all_listings
