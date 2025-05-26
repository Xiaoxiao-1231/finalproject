# 🌍 Scientific Programming Final Project

**Author:** Xiao Zhou  
**Date:** May 2025

This project focuses on scraping climate-related news from **BBC** and **CNN**, extracting full content, identifying country/location mentions, and applying sentiment analysis.

---

## 📁 BBC Workflow

### 1. Scraping News Titles & Links
- **Script:** `bbc_scraper.py`
- **Output:** `BBC_Climate_Articles_Limited.csv`  
- **Note:** Pagination was done manually; total 403 articles scraped.

### 2. Scraping Full Article Content
- **Script:** `bbc_content.py`
- **Output:** `bbc_climate_articles_with_content.csv`

### 3. Sentiment Analysis
- **Script:** `senti_local_bbc.py`
- **Output:** `sentiment_bbc.csv`

---

## 📁 CNN Workflow

### 1. Scraping News Titles & Links
- **Script:** `cnn.py`
- **Output:** `cnn.csv`

### 2. Scraping Full Article Content
- **Script:** `cnn_content.py`
- **Output:** `cnn_content.csv`

### 3. Sentiment Analysis
- **Script:** `senti_local_cnn.py`
- **Output:** `sentiment_cnn.csv`

---

## 🧠 Libraries Used

- `selenium` + `webdriver_manager` – for dynamic page scraping
- `spaCy` – for country/location name recognition
- `vaderSentiment` – for sentiment scoring

---

## 📚 Development Log

See process book for a complete log of project progress, challenges, and code updates.
And see report for some findings and detailed actions

