import pandas as pd
<<<<<<< HEAD
=======
# import numpy as n
# import text2emotion as te
# from dotenv import load_dotenv
>>>>>>> c3d1b4dcf685d83076cfc8e768dc4dc50e1da86f
from googleapiclient.discovery import build
# from iteration_utilities import unique_everseen
from utils.comments import process_comments, make_csv

<<<<<<< HEAD
API_KEY = "AIzaSyDSLbJActSbVC0x97sbo_dpxfkP7dYCqB0"
youtube = build("youtube", "v3", developerKey=API_KEY)

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
   

def main():
  
   # extracting all video ids from dataset
=======
# API_KEY = "AIzaSyA5pIGUOIuLyFgf2BK7MCyiOFXmIUg9Gl8"
API_KEY = "AIzaSyDSLbJActSbVC0x97sbo_dpxfkP7dYCqB0"
youtube = build("youtube", "v3", developerKey=API_KEY)


# def video_threads(videoIDs):
#     comments_list = []
#     for videoID in videoIDs:
#         request = youtube.commentThreads().list(
#             part='id, snippet',
#             videoId=videoID,
#             maxResults=100
#         )
#         response = request.execute()
#         comments_list.extend(process_comments(response['items']))
#     return comments_list


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
    # print(response.keys())
    # print(response)
    # print(comments_list)


def main():
    # vid_id = input("Enter video ID: ")
    videoID = "2kyS6SvSYSE"
    # make_csv(comment_threads(videoID))
    # you just need to replace the following array with an array that contains all the video id's from the database.
    videoIDs = ["puqaWrEC7tY", "d380meD0W0M",
                "gHZ1Qz0KiKM", "39idVpFF7NQ", "nc99ccSXST0"]

    # extracting all video ids from dataset
>>>>>>> c3d1b4dcf685d83076cfc8e768dc4dc50e1da86f
    us_url = 'https://raw.githubusercontent.com/MayurDeshmukh10/youtube_analysis/master/USvideos.csv'
    us_data = pd.read_csv(us_url)
    video_ids = us_data['video_id'].tolist()

<<<<<<< HEAD
    print('video ids:')
    print(len(video_ids))
    unique_video_ids = list(set(video_ids))

    print('unique video ids:')
    print(len(unique_video_ids))
    make_csv(video_threads(unique_video_ids))
    
=======
    # print(video_ids)
    print('video ids:')
    print(len(video_ids))
    unique_video_ids = list(set(video_ids))
    # print(unique_video_ids)
    print('unique video ids:')
    print(len(unique_video_ids))

    # make_csv(video_threads(videoIDs))
    make_csv(video_threads(unique_video_ids))


>>>>>>> c3d1b4dcf685d83076cfc8e768dc4dc50e1da86f
if __name__ == "__main__":
    main()
