import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#BBC news link for climate section
base_url = "https://www.bbc.com/news/science_and_environment"

#scrape articles from given URL
def scrape_articles(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all articles in the Earth section
    articles = soup.find_all('a', class_='gs-c-promo-heading')

    article_data = []

    for article in articles:
        title = article.get_text()
        link = article['href']
        # Ensure that links are absolute URLs
        if link.startswith('/'):
            link = 'https://www.bbc.com' + link

        # Try to find the publication date
        time_tag = article.find_next('time')
        if time_tag:
            time_str = time_tag.get_text()
            try:
                pub_time = datetime.strptime(time_str, "%d %b %Y")  # Format example: 25 Oct 2024
            except ValueError:
                pub_time = "N/A"
        else:
            pub_time = "N/A"

        article_data.append([title, link, pub_time])

    return article_data

# Function to save the scraped data to CSV
def save_to_csv(data, filename="bbc_earth_articles_2024.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link", "Publication Time"])
        writer.writerows(data)

# Scrape the articles from BBC Earth section and save to CSV
article_data = scrape_articles(base_url)
save_to_csv(article_data)

print("Scraping complete! The data has been saved to 'bbc_earth_articles_2024.csv'.")
