from comment_reader import non_comment, us_comments

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def main():
    
    text = TextBlob(us_comments())
    print(text.sentiment)

if __name__ == '__main__':
    main()