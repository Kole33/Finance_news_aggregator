import feedparser

SOURCES = [
    'https://feeds.reuters.com/reuters/businessNews',
    'https://www.investopedia.com/news/rss/',
    'https://www.bloomberg.com/feeds/bbiz/sitemap_index.xml',
    'https://finance.yahoo.com/rss/'
]

def fetch_news_from_rss():
    news_list = []
    
    for RSS_FEED_URL in SOURCES:
        feed = feedparser.parse(RSS_FEED_URL)
        for entry in feed.entries:
            news_list.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.published
            })
    
    return news_list
