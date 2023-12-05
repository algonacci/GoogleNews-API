from pygooglenews import GoogleNews

# Initialize GoogleNews with Indonesian language and country settings
gn = GoogleNews(lang='id', country='id')

# Search for news articles about Jakarta
search_results = gn.search('jakarta')

# Extract and print the title and source of each news article
for entry in search_results['entries']:
    title = entry.title
    source = entry.source.title
    print(f"Title: {title}\nSource: {source}\n")
