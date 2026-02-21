# Sentiment Analysis: Is a Tweet Positive or Negative? 🐦 (Day 64)
# pip install textblob matplotlib
# python -m textblob.download_corpora

from textblob import TextBlob
import matplotlib.pyplot as plt

print("=" * 60)
print("🐦 Tweet Sentiment Analyzer | Day 64")
print("=" * 60)

# --- Sample Tweets for Batch Analysis ---
sample_tweets = [
    "I absolutely love Python! Best programming language ever! 🔥",
    "This weather is terrible, ruined my whole day 😤",
    "Just had an amazing coffee at the new cafe downtown ☕",
    "The movie was okay, nothing special honestly",
    "I can't believe how bad the customer service was. Never going back!",
    "Congratulations to the team on the incredible product launch! 🚀",
    "Stuck in traffic for 2 hours. What a waste of time.",
    "Learning Machine Learning is so exciting and fun! 🤖",
    "The food was bland and overpriced. Very disappointed.",
    "What a beautiful sunset today! Nature is amazing 🌅",
]


def analyze_sentiment(text):
    """Analyze sentiment of a text and return polarity, subjectivity, and label."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity        # -1 (negative) to +1 (positive)
    subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)

    if polarity > 0.1:
        label = "Positive"
        emoji = "😊"
    elif polarity < -0.1:
        label = "Negative"
        emoji = "😡"
    else:
        label = "Neutral"
        emoji = "😐"

    return polarity, subjectivity, label, emoji


# --- Batch Analysis ---
print("\n📊 BATCH ANALYSIS OF SAMPLE TWEETS:")
print("-" * 60)

positive, negative, neutral = 0, 0, 0
polarities = []
labels_list = []

for i, tweet in enumerate(sample_tweets, 1):
    polarity, subjectivity, label, emoji = analyze_sentiment(tweet)
    polarities.append(polarity)
    labels_list.append(label)

    # Count sentiments
    if label == "Positive":
        positive += 1
    elif label == "Negative":
        negative += 1
    else:
        neutral += 1

    # Polarity bar (visual representation)
    bar_pos = int((polarity + 1) * 15)  # map -1..+1 to 0..30
    bar = "▓" * bar_pos + "░" * (30 - bar_pos)

    print(f"\n{emoji} Tweet #{i}: \"{tweet[:50]}{'...' if len(tweet) > 50 else ''}\"")
    print(f"   Polarity: [{bar}] {polarity:+.2f}")
    print(f"   Subjectivity: {subjectivity:.2f} | Label: {label}")

# --- Summary ---
total = len(sample_tweets)
print("\n" + "=" * 60)
print("📈 SENTIMENT SUMMARY:")
print(f"   😊 Positive: {positive}/{total} ({positive/total*100:.0f}%)")
print(f"   😐 Neutral:  {neutral}/{total} ({neutral/total*100:.0f}%)")
print(f"   😡 Negative: {negative}/{total} ({negative/total*100:.0f}%)")
print("=" * 60)

# --- Visualization ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Tweet Sentiment Analysis - Day 64", fontsize=14, fontweight='bold')

# Bar Chart: Sentiment Distribution
colors_bar = ['#2ecc71', '#f39c12', '#e74c3c']
counts = [positive, neutral, negative]
labels_bar = ['😊 Positive', '😐 Neutral', '😡 Negative']
axes[0].bar(labels_bar, counts, color=colors_bar, edgecolor='black', linewidth=0.5)
axes[0].set_title("Sentiment Distribution")
axes[0].set_ylabel("Number of Tweets")

# Scatter Plot: Polarity of each tweet
colors_scatter = ['#2ecc71' if p > 0.1 else '#e74c3c' if p < -0.1 else '#f39c12' for p in polarities]
axes[1].bar(range(1, len(polarities) + 1), polarities, color=colors_scatter, edgecolor='black', linewidth=0.5)
axes[1].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
axes[1].set_title("Polarity per Tweet")
axes[1].set_xlabel("Tweet #")
axes[1].set_ylabel("Polarity (-1 to +1)")

plt.tight_layout()
plt.savefig("sentiment_chart.png", dpi=150)
print("\n📊 Chart saved as 'sentiment_chart.png'")
plt.show()

# --- Interactive Mode ---
print("\n" + "=" * 60)
print("✍️  INTERACTIVE MODE: Type your own tweet to analyze!")
print("   Type 'quit' to exit\n")

while True:
    user_tweet = input("🐦 Enter a tweet: ").strip()
    if user_tweet.lower() in ['quit', 'exit', 'q']:
        print("\n👋 Thanks for using the Sentiment Analyzer! See you on Day 65!")
        break
    if not user_tweet:
        continue

    polarity, subjectivity, label, emoji = analyze_sentiment(user_tweet)
    print(f"   {emoji} Sentiment: {label}")
    print(f"   📊 Polarity: {polarity:+.2f} | Subjectivity: {subjectivity:.2f}\n")