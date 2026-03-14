from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///research.db")


def create_table():

    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS research_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            result TEXT
        )
        """))
def save_query(query, result):

    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO research_history (query, result) VALUES (:q, :r)"),
            {"q": query, "r": result}
        )