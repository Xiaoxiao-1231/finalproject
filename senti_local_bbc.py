import pandas as pd
import spacy
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load spaCy model and VADER
nlp = spacy.load("en_core_web_sm")
analyzer = SentimentIntensityAnalyzer()

# Clean helper function
def clean_text(text):
    text = str(text)
    # 移除包含特定广告/推广内容的行
    removal_keywords = [
        "Sign up for our Future Earth newsletter",
        "Outside the UK? Sign up to our international newsletter"
    ]
    for keyword in removal_keywords:
        text = text.replace(keyword, "")
    return text

# Read content CSV
df = pd.read_csv("bbc_climate_articles_with_content.csv")

#  Clean text content
df["CleanedContent"] = df["Content"].apply(clean_text)

#  Sentiment score using cleaned content
df["SentimentScore"] = df["CleanedContent"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])

#  Country-based sentiment accumulation
country_sentiment = defaultdict(list)

for _, row in df.iterrows():
    doc = nlp(str(row["CleanedContent"]))
    sentiment = row["SentimentScore"]
    countries = set(ent.text for ent in doc.ents if ent.label_ == "GPE")
    for country in countries:
        country_sentiment[country].append(sentiment)

# Sentiment summary per country
summary = [{
    "Country": country,
    "Mentions": len(scores),
    "AverageSentiment": sum(scores) / len(scores)
} for country, scores in country_sentiment.items() if len(scores) >= 2]

#  Output CSV
country_df = pd.DataFrame(summary).sort_values(by="AverageSentiment")
country_df.to_csv("sentiment_bbc.csv", index=False, float_format="%.4f")

print("✅ Sentiment file saved as: sentiment_bbc.csv")
