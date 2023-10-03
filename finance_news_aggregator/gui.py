import tkinter as tk
from tkinter import ttk, scrolledtext, Menu
import data_storage

def copy_text(event):
    """Handles the Copy operation for the text area."""
    selected_text = event.widget.get(tk.SEL_FIRST, tk.SEL_LAST)
    event.widget.clipboard_clear()
    event.widget.clipboard_append(selected_text)
    event.widget.update()

def display_enhanced_gui():
    window = tk.Tk()
    window.title("Finance News Aggregator")

    frame = ttk.Frame(window, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    label = ttk.Label(frame, text="Finance News", font=('Arial', 24, 'bold'))
    label.grid(row=0, column=0, sticky=tk.W, pady=5)

    text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=('Arial', 12))
    text_area.grid(row=1, column=0, pady=5, sticky=tk.NSEW)

    # Add a context menu for copying
    context_menu = Menu(text_area, tearoff=0)
    context_menu.add_command(label="Copy", command=lambda: copy_text(text_area))
    text_area.bind("<Button-3>", lambda e: context_menu.post(e.x_root, e.y_root))

    # Configure the grid weights
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    populate_text_area_with_news(text_area)

    # Button to show only important news in a new window
    btn_show_important = ttk.Button(frame, text="Show Important News", command=show_important_news)
    btn_show_important.grid(row=2, column=0, pady=10)

    window.mainloop()

def show_important_news():
    important_window = tk.Toplevel()
    important_window.title("Important Finance News")

    # Make the window resizable
    important_window.geometry("800x600")  # Set a default size (optional)
    important_window.minsize(300, 300)    # Set a minimum size (optional)
    
    frame = ttk.Frame(important_window, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    label = ttk.Label(frame, text="Important News", font=('Arial', 24, 'bold'))
    label.grid(row=0, column=0, sticky=tk.W, pady=5)

    text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=('Arial', 12))
    text_area.grid(row=1, column=0, pady=5, sticky=tk.NSEW)

    # Configure the grid weights
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Only populate with important news
    important_keywords = [
    "stock market", "interest rate", "economic downturn", "recession", "decline",
    "crisis", "inflation", "deflation", "bankruptcy", "merger", "acquisition",
    "federal reserve", "unemployment", "trade war", "tariffs", "GDP", "economic growth",
    "bear market", "bull market", "IPO", "default", "debt ceiling", "brexit", "stimulus",
    "bailout", "sanctions", "rate hike", "rate cut", "dow jones", "nasdaq", "s&p 500"
]
    news_list = data_storage.fetch_all_news()
    important_news = [news for news in news_list if any(keyword in news[1].lower() for keyword in important_keywords)]
    populate_text_area_with_news(text_area, important_news)


def populate_text_area_with_news(text_area, news_list=None):
    if news_list is None:
        news_list = data_storage.fetch_all_news()

    # Keywords for sentiment analysis (customize these lists as needed)
    negative_keywords = ["crash", "fall", "downturn", "recession", "decline"]
    positive_keywords = ["rise", "increase", "boom", "growth", "profit"]

    for news in news_list:
        sentiment = "neutral"
        for keyword in negative_keywords:
            if keyword in news[1].lower():
                sentiment = "negative"
                break
        for keyword in positive_keywords:
            if keyword in news[1].lower():
                sentiment = "positive"
                break

        # Apply color and style based on sentiment
        if sentiment == "negative":
            text_area.insert(tk.END, f"Title: {news[1]}\n", "negative")
        elif sentiment == "positive":
            text_area.insert(tk.END, f"Title: {news[1]}\n", "positive")
        else:
            text_area.insert(tk.END, f"Title: {news[1]}\n", "neutral")

        text_area.insert(tk.END, f"Link: {news[2]}\n")
        text_area.insert(tk.END, f"Published: {news[3]}\n\n")

    # Configuring tags for different sentiments
    text_area.tag_configure("neutral", foreground="blue", font=('Arial', 12, 'bold'))
    text_area.tag_configure("negative", foreground="red", font=('Arial', 12, 'bold'))
    text_area.tag_configure("positive", foreground="green", font=('Arial', 12, 'bold'))




