# twitterSentimentAnalyticsBot
Scrape twitter for tags/keywords and send sentiment analytics via email.

Settings:
1. Fill in the consumer keys and access tokens for twitter in config.py
2. Fill in the email address and password of your test account which sends email in config.py
(Use a test account with reduced security settings to enable smtp to work with yahoo or google)
3. Fill in the recipient email address to receive the daily sentiment analysis data

Result example for "bitcoin":
Negative tweets: 91.73
Positive tweets: 199.14
Neutral tweets: 1709.113
Polarity: 221.83
