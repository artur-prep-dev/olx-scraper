from scraper import scrape_category
from database import create_connection, create_table, insert_listing
from cleaner import clean_listing
import pandas as pd

# TODO: przeniesc kategorie do osobnego pliku konfiguracyjnego
CATEGORIES = {
    "nieruchomosci": "https://www.olx.pl/nieruchomosci/",
    "elektronika": "https://www.olx.pl/elektronika/",
}

def main():
    print("Uruchamiam scraper OLX...")

    conn = create_connection()
    create_table(conn)

    total_saved = 0

    for category, url in CATEGORIES.items():
        print(f"\nKategoria: {category.upper()}")

        raw_listings = scrape_category(url, category, max_pages=2)

        for raw in raw_listings:
            cleaned = clean_listing(raw)
            insert_listing(conn, cleaned)
            total_saved += 1

        print(f"Zapisano {len(raw_listings)} ogloszen z kategorii: {category}")

    print(f"\nGotowe! Lacznie zapisano: {total_saved} ogloszen")

    export_to_csv(conn)
    conn.close()

def export_to_csv(conn):
    df = pd.read_sql_query("SELECT * FROM listings", conn)
    # utf-8-sig zeby polskie znaki dobrze otwieraly sie w Excelu
    df.to_csv("olx_data.csv", index=False, encoding="utf-8-sig")
    print("Dane wyeksportowane do olx_data.csv")

if __name__ == "__main__":
    main()
