import sqlite3
from datetime import datetime
from pathlib import Path

# Creăm baza de date în același director cu fișierul Python (dacă nu există deja)
DB_PATH = Path(__file__).resolve().parent.parent / "requests.db"
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# Cream tabelul dacă nu există deja
cursor.execute("""
CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    operation TEXT,
    inputs TEXT,
    result TEXT
)
""")

conn.commit()


def save_request(operation: str, inputs: list[int], result: str):
    cursor.execute("""
        INSERT INTO requests (timestamp, operation, inputs, result)
        VALUES (?, ?, ?, ?)
    """, (datetime.now().isoformat(), operation, str(inputs), result))
    conn.commit()
