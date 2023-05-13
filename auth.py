import pandas as pd
import csv


try:
   # to read count csv, should maintain usecols becasue commas are inside string, otherwise will crash
   # i included to_csv to save the clipped data that works for us
   count_data = pd.read_csv('/Users/iris/Documents/Hunter/SPRING_2023/nlp/final_proj/data/USvideos.csv', usecols=['video_id','title','channel_title','views','likes','dislikes','comment_total'])
   
   # to open comment data
   # this returns an onject, so print() wont work
   with open('/Users/iris/Documents/Hunter/SPRING_2023/nlp/final_proj/data/UScomments.csv', 'r') as f:
      comments_data = csv.reader(f)

except Exception as e:
    print('error in the read_csv')


print(count_data[:5])
print(comments_data)

#count_data.to_csv('clean_vid.csv', index=False)