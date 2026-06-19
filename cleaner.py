import re

def clean_price(price_str):
    if not price_str:
        return None
    # usuwa "zl", spacje i inne znaki - zostawia tylko cyfry
    cleaned = re.sub(r"[^\d,.]", "", price_str)
    cleaned = cleaned.replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        # zwraca None dla ofert typu "Zamienie", "Do negocjacji"
        return None

def clean_title(title):
    if not title:
        return None
    return title.strip()

def clean_location(location):
    if not location:
        return None
    return location.strip()

def clean_listing(listing):
    return {
        "title": clean_title(listing.get("title")),
        "price": clean_price(listing.get("price")),
        "location": clean_location(listing.get("location")),
        "date_added": listing.get("date_added", "").strip(),
        "url": listing.get("url", "").strip(),
        "category": listing.get("category", "").strip()
    }
