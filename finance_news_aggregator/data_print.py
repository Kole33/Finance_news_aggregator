import sqlite3

DATABASE_NAME = 'aggregator.db'

def print_news():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM news')
    all_news = cursor.fetchall()
    for news in all_news:
        print(f"Title: {news[1]}")
        print(f"Link: {news[2]}")
        print(f"Published: {news[3]}\n")
    conn.close()

