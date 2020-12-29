from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAnalyser():
    def __init__(self):
        self.polarity = 0
        self.score = {}

    def textAnalyze(self, text):
        analysis = TextBlob(text)
        self.polarity = analysis.sentiment.polarity
        self.score = SentimentIntensityAnalyzer().polarity_scores(text)
