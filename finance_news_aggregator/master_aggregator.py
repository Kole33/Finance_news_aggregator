
import aggregator
import data_storage
import data_print
import gui

def main():
    # Fetch news
    news_list = aggregator.fetch_news_from_rss()
    
    # Setup database and store news
    data_storage.setup_database()
    data_storage.store_news(news_list)

    # Print news in console
    data_print.print_news()

    # Display GUI
    gui.display_enhanced_gui()

if __name__ == "__main__":
    main()
