# twitterSentimentAnalyticsBot
Scrape twitter for tags/keywords and send sentiment analytics via email.

Settings:
1. Fill in the consumer keys and access tokens for twitter in config.py
2. Fill in the email address and password of your test account which sends email in config.py
(Use a test account with reduced security settings to enable smtp to work with yahoo or google)
3. Fill in the recipient email address to receive the daily sentiment analysis data

The Bot will scrape tweets using the keyword for the last 24 hours, filtering retweets. This list will then be analyzed using NLTK vader and Textblob to 
provide sentiment in the form of negative tweets, positive tweets and neutral tweets. Emojis are not analyzed. Polarity is provided seperately to indicate the overall sentiment.

Result for example
Keywords: "Lockdown London"

Negative tweets: 6.85% 
Positive tweets: 7.18% 
Neutral tweets: 85.97% 
Polarity: 7.79
