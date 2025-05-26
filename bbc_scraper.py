from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Create an empty dictionary to store the scraped data
data_dict = {
    "Title": [],
    "Time": [],
    "Link": []
}

# Set a limit for the number of articles to scrape
MAX_ARTICLES = 100
article_count = 0

try:
    # Step 1: Open the BBC homepage
    driver.get("https://www.bbc.com/")
    time.sleep(5)  # Wait for the page to load

    # Step 2: Click on the search button
    search_button = driver.find_element(By.XPATH, '//button[@aria-label="Search BBC"]')
    search_button.click()
    time.sleep(2)

    # Step 3: Enter the search term "Climate"
    search_input = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[6]/div/div[1]/div/input')
    search_input.send_keys("Climate")
    search_input.send_keys(Keys.RETURN)
    time.sleep(15)  # Wait for search results to load

    # Scrape data from the current page
    while article_count < MAX_ARTICLES:
        # Parse the current page with BeautifulSoup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # Extract articles from the page
        articles = soup.find_all("div", {"data-testid": "newport-card"})
        if not articles:
            print("No articles found on this page. Breaking.")
            break  # Stop scraping if no articles found

        for article in articles:
            if article_count >= MAX_ARTICLES:
                break  # Stop if we have scraped enough articles

            # Extract title
            title = article.find("h2").get_text().strip() if article.find("h2") else "No title available"

            # Extract time
            time_info = article.find("span", {"data-testid": "card-metadata-lastupdated"}).get_text().strip() if article.find("span", {"data-testid": "card-metadata-lastupdated"}) else "No time available"

            # Extract link
            link_element = article.find("a", href=True)
            link = f"https://www.bbc.com{link_element['href']}" if link_element else "No link available"

            # Append data to dictionary
            data_dict["Title"].append(title)
            data_dict["Time"].append(time_info)
            data_dict["Link"].append(link)

            article_count += 1  # Increment the count

        # Print the progress so far
        print(f"Scraped {article_count} articles")

        # Wait for you to manually click the "Next page" button
        if article_count < MAX_ARTICLES:
            input("Press Enter after manually navigating to the next page...")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Save data to a CSV file
    df = pd.DataFrame(data_dict)
    df.to_csv("BBC_Climate_Articles_Limited.csv", index=False)
    print(f"Data saved to BBC_Climate_Articles_Limited.csv with {article_count} articles.")

    # Quit the driver
    driver.quit()
