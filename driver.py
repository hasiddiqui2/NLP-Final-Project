from methods import us_comments, us_videos, process_comment_data, agregate_sentiments, merger
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import csv

def main():
    # Initialize the VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    comment_data = us_comments()
    polarity_score_list = []

    for comment in comment_data:
        text = comment[1]
        
        # contains pos, neg, and compund scores
        all_scores_for_comment = analyzer.polarity_scores(text)

        # extract only compound scores from the dict
        compound_score = all_scores_for_comment['compound']

        polarity_score_list.append([comment[0],comment[1],compound_score])


    # Write the list to a CSV file
    with open('comment_polarity.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(polarity_score_list)

    
    
    my_videos = us_videos()
    us_video_id_list = list(my_videos['video_id'])
    
    comment_list, comment_map = process_comment_data(comment_data)
    usable_vid_count = 0
    unusable_vid_count = 0
    for key in comment_map:
        if key in us_video_id_list:
            usable_vid_count += 1
        else:
            unusable_vid_count += 1
    print(usable_vid_count)
    print(unusable_vid_count)
    
    agregate_sentiments(comment_map, polarity_score_list)

    # merges the USvideo.csv and agregate_sentiment's csv
    merger()
if __name__ == '__main__':
    main()