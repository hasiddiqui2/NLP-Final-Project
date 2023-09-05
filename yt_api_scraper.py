import pandas as pd
from googleapiclient.discovery import build
from utils.comments import process_comments, make_csv

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
               maxResults=100,
               order="relevance"
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
    us_url = 'https://raw.githubusercontent.com/MayurDeshmukh10/youtube_analysis/master/USvideos.csv'
    us_data = pd.read_csv(us_url)
    video_ids = us_data['video_id'].tolist()

    print('video ids:')
    print(len(video_ids))
    unique_video_ids = list(set(video_ids))

    print('unique video ids:')
    print(len(unique_video_ids))
    make_csv(video_threads(unique_video_ids))
    
if __name__ == "__main__":
    main()
