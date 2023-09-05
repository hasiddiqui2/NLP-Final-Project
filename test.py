from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

#text= "I need yall to stop, u got me staying up to late replayin' this......"
#text = "YES!"
text = "NERVOUS CHANGING DIRECTION FROM OFFICERS RUNNING"
text1 = 'COOPERATIVE'
blob = TextBlob(text1)

# Perform spellcheck
corrected_text = blob.correct()

polar = analyzer.polarity_scores(text1)

print(corrected_text)
print(polar)
