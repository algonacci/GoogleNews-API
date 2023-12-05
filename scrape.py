from bs4 import BeautifulSoup
import requests

# Define the Google News RSS URL for Indonesian news
google_news_indonesia_url = "https://news.google.com/rss?hl=id&gl=ID&ceid=ID:id"

# Request the page content
xml_page = requests.get(google_news_indonesia_url).content

# Parse the content using BeautifulSoup
soup_page = BeautifulSoup(xml_page, "xml")

# Find all news items
news_items = soup_page.find_all("item")

# Define the keyword you want to search for
search_keyword = "Gibran"  # Replace with your specific keyword

# Extract news items that contain the keyword
filtered_news = []
for item in news_items:
    title = item.title.text if item.title else "N/A"
    # Check if the keyword is in the title
    if search_keyword.lower() in title.lower():
        # Extracting the news link and publication date (optional)
        link = item.link.text if item.link else "N/A"
        pubDate = item.pubDate.text if item.pubDate else "N/A"
        filtered_news.append(
            {"Title": title, "Link": link, "Published Date": pubDate})

# Display the first few news items that match the keyword
for news in filtered_news[:5]:
    print(
        f"Title: {news['Title']}")
