import sqlite3

DATABASE_NAME = 'aggregator.db'

def setup_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY,
        title TEXT,
        link TEXT,
        published TEXT
    )
    ''')
    conn.commit()
    conn.close()

def store_news(news_list):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    for news in news_list:
        cursor.execute('''
        INSERT INTO news (title, link, published)
        VALUES (?, ?, ?)
        ''', (news['title'], news['link'], news['published']))
    conn.commit()
    conn.close()

def fetch_all_news():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM news')
    all_news = cursor.fetchall()
    
    conn.close()
    return all_news

