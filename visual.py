import pandas as pd
import matplotlib.pyplot as plt

# Read files
bbc_df = pd.read_csv("sentiment_bbc.csv")
cnn_df = pd.read_csv("sentiment_cnn.csv")

# BBC
bbc_sorted = bbc_df.sort_values(by="AverageSentiment")

plt.figure(figsize=(14, 6))
plt.barh(bbc_sorted["Country"], bbc_sorted["AverageSentiment"], color="skyblue")
plt.title("BBC - Average Sentiment by Lables")
plt.xlabel("Average Sentiment Score")
plt.ylabel("Lable")
plt.tight_layout()
plt.savefig("bbc_sentiment.png", dpi=300)  # 自动保存图像
plt.show()

# CNN
cnn_sorted = cnn_df.sort_values(by="AverageSentiment")

plt.figure(figsize=(14, 6))
plt.barh(cnn_sorted["Country"], cnn_sorted["AverageSentiment"], color="lightcoral")
plt.title("CNN - Average Sentiment by Lables")
plt.xlabel("Average Sentiment Score")
plt.ylabel("Lable")
plt.tight_layout()
plt.savefig("cnn_sentiment.png", dpi=300)  # 自动保存图像
plt.show()
