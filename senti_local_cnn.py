import pandas as pd
import spacy
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# load model
nlp = spacy.load("en_core_web_sm")
analyzer = SentimentIntensityAnalyzer()

# read the file,i change it manually, to do sentiment analysis on both two files
df = pd.read_csv("cnn_content.csv")

# define sentiment
df["SentimentScore"] = df["Content"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])

# country —— sentiment
country_sentiment = defaultdict(list)

for _, row in df.iterrows():
    doc = nlp(str(row["Content"]))
    sentiment = row["SentimentScore"]

    #  get unique place names
    countries = set(ent.text for ent in doc.ents if ent.label_ == "GPE")
    for country in countries:
        country_sentiment[country].append(sentiment)

#  get the sentiment table
summary = [{
    "Country": country,
    "Mentions": len(scores),
    "AverageSentiment": sum(scores) / len(scores)
} for country, scores in country_sentiment.items() if len(scores) >= 2]

# out put CSV
country_df = pd.DataFrame(summary).sort_values(by="AverageSentiment")
country_df.to_csv("sentiment_cnn.csv", index=False, float_format = "%.4f")

print("saved to sentiment_cnn.csv")
