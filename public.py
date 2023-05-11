# import os
# # import pandas as pd
# # import numpy as n
# #import text2emotion as te
# #from dotenv import load_dotenv
# from googleapiclient.discovery import build
# #from iteration_utilities import unique_everseen
# from utils.comments import process_comments, make_csv

# API_KEY = "AIzaSyA5pIGUOIuLyFgf2BK7MCyiOFXmIUg9Gl8"
# youtube = build("youtube", "v3", developerKey=API_KEY)

# def comment_threads(channelID, to_csv=True):
#    comments_list = []
#    request = youtube.commentThreads().list(
#       part='id,replies,snippet',
#       videoId=channelID,
#       #maxResults = 5
#       )
#    response = request.execute()
#    comments_list.extend(process_comments(response['items']))

#    if to_csv():
#       make_csv(comments_list, channelID)

#    return comments_list
#    #print(response.keys())
#    # print(response)
#    #print(comments_list)

# def main():
#    #vid_id = input("Enter video ID: ")
#    comment_threads("2kyS6SvSYSE", to_csv=True)

# if __name__ == "__main__":
#    main()

import os
import pandas as pd
# import numpy as n
#import text2emotion as te
#from dotenv import load_dotenv
from googleapiclient.discovery import build
#from iteration_utilities import unique_everseen
from utils.comments import process_comments, make_csv

API_KEY = "AIzaSyA5pIGUOIuLyFgf2BK7MCyiOFXmIUg9Gl8"
youtube = build("youtube", "v3", developerKey=API_KEY)

def video_threads(videoIDs):
   comments_list = []
   for videoID in videoIDs:
      request = youtube.commentThreads().list(
         part='id, snippet',
         videoId=videoID,
         maxResults = 100
         )
      response = request.execute()
      comments_list.extend(process_comments(response['items']))
   return comments_list

def video_threads(videoIDs):
   comments_list = []
   inaccessible_vid_ids = []
   for videoID in videoIDs:
      try:
         request = youtube.commentThreads().list(
               part='id, snippet',
               videoId=videoID,
               maxResults=100
         )
         response = request.execute()
         comments_list.extend(process_comments(response['items']))
      except Exception as e:
         # print(f"Error processing video ID {videoID}: {e}")
         inaccessible_vid_ids.append(videoID)
         continue
   print('the following vids could not be accessed:')
   print(inaccessible_vid_ids)
   return comments_list
   #print(response.keys())
   # print(response)
   #print(comments_list)

def main():
   #vid_id = input("Enter video ID: ")
   videoID = "2kyS6SvSYSE"
   # make_csv(comment_threads(videoID))
   # you just need to replace the following array with an array that contains all the video id's from the database. 
   videoIDs = ["puqaWrEC7tY", "d380meD0W0M", "gHZ1Qz0KiKM", "39idVpFF7NQ", "nc99ccSXST0"]
   
   #extracting all video ids from dataset
   us_url = 'https://raw.githubusercontent.com/MayurDeshmukh10/youtube_analysis/master/USvideos.csv'
   us_data = pd.read_csv(us_url)
   video_ids = us_data['video_id'].tolist()
   # print(video_ids)
  
   #make_csv(video_threads(videoIDs))
   make_csv(video_threads(video_ids))
if __name__ == "__main__":
   main()