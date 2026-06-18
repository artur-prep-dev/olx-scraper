import sqlite3

def create_connection():
    conn = sqlite3.connect("olx_data.db")
    return conn

def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS listings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        price REAL,
        location TEXT,
        date_added TEXT,
        url TEXT UNIQUE,
        category TEXT,
        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    conn.execute(query)
    conn.commit()
    print("Tabela utworzona!")

def insert_listing(conn, listing):
    query = """
    INSERT OR IGNORE INTO listings 
    (title, price, location, date_added, url, category)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    try:
        conn.execute(query, (
            listing["title"],
            listing["price"],
            listing["location"],
            listing["date_added"],
            listing["url"],
            listing["category"]
        ))
        conn.commit()
    except Exception as e:
        print(f"Blad przy zapisie: {e}")

def get_all_listings(conn):
    query = "SELECT * FROM listings"
    cursor = conn.execute(query)
    return cursor.fetchall()
