import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import os

# load csv
source_file = "bbc_climate_search_results.csv"

# output
output_file = "bbc_climate_articles_with_content.csv"


# load
df = pd.read_csv(source_file)
df["Content"] = ""

# scrape article
for i, row in df.iterrows():
    url = row["Link"]
    print(f"🔍 scraping...：{url}")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        article_tag = soup.find("article")
        if article_tag:
            paragraphs = article_tag.find_all("p")
        else:
            paragraphs = soup.find_all("p")

        content = "\n".join([p.get_text().strip() for p in paragraphs])
        df.at[i, "Content"] = content
        print(f"✅ scraping article succesfully，this is the {i+1}/{len(df)} ")

    except Exception as e:
        print(f"❌ error：{e}")
        df.at[i, "Content"] = "ERROR"

    time.sleep(1.2)

# save
df.to_csv(output_file, index=False)
print(f"\n📁 content saved to!：{output_file}")
