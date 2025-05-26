from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd


def extract_visible_articles():
    title_list = []
    link_list = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    for i in range(1,60):
        p = 10*(i-1)
        #
#        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        url = f"https://edition.cnn.com/search?q=climate+solution&from={p}&size=10&page={i}&sort=newest&types=article&section="
        driver.get(url)
#        driver.get("https://edition.cnn.com/search?q=climate+solution&from=0&size=10&page=" + str(i) + "&sort=newest&types=article&section=")

        # wait
        time.sleep(5)

        # get html
        html = driver.page_source


        soup = BeautifulSoup(html, "html.parser")

        # get all container__headline-text
        spans = soup.find_all("span", class_="container__headline-text")
        df = []
        for i, span in enumerate(spans, 1):
            title = span.text.strip()
            link = span.get("data-zjs-href")
            title_list.append(title)
            link_list.append(link)

        df = pd.DataFrame({
        "Title": title_list,
        "Link": link_list
    })
    driver.quit()
    return df

datas = extract_visible_articles()
datas.to_csv("cnn.csv",index=False)
