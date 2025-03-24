import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://news.ycombinator.com/"

# Request the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract news titles and links
articles = soup.select('.athing')
data = []

for article in articles:
    title = article.select_one('.titleline a').text
    link = article.select_one('.titleline a')['href']
    data.append([title, link])

# Save data as CSV
df = pd.DataFrame(data, columns=['Title', 'Link'])
df.to_csv("hacker_news.csv", index=False)

print("CSV file saved successfully!")
