import pandas as pd
import csv

with open('/Users/iris/Documents/Hunter/SPRING_2023/nlp/final_proj/data/UScomments.csv', mode='r', encoding='utf-8-sig') as infile:
    reader = csv.reader(infile, quoting=csv.QUOTE_ALL)
    header_data = list(next(reader))
    infile = infile.read().replace('\0', '').splitlines()
    reader2 = csv.reader(infile)
    reader3 = list(reader2)
print(reader3[:3])

# try:
#     with open('/Users/iris/Documents/Hunter/SPRING_2023/nlp/final_proj/data/UScomments.csv', 'rb') as infile:
#       data = infile.read()
#       data = data.replace(b'\x00', b'')

#     with open('file_clean.csv', 'wb') as outfile:
#       outfile.write(data)

#     with open('file_clean.csv', 'r') as csvfile:
#       csvreader = csv.reader(csvfile)
#       for row in csvreader:
#         # Do something with the rows
#         # f_data = pd.DataFrame(row[[1:]], columns=row[[0]])
#         comment_data = pd.DataFrame(row, columns=['video_id', 'comment_text', 'likes', 'replies'])

#       print(comment_data.tail())
#         #print(comment_data.columns)


# except Exception as e:
#   print('ERROR in csv read')

# #print(count_data[:5])

# to read count csv, should maintain usecols becasue commas are inside string, otherwise will crash
   # i included to_csv to save the clipped data that works for us
   #count_data = pd.read_csv('/Users/iris/Documents/Hunter/SPRING_2023/nlp/final_proj/data/USvideos.csv', usecols=['video_id','title','channel_title','views','likes','dislikes','comment_total'])
   
   # to open comment data
   # this returns an onject, so print() wont work

# try:
#   with open('/Users/iris/Documents/Hunter/SPRING_2023/nlp/final_proj/data/UScomments.csv', 'r') as f:
#     comments_data = csv.reader(f)
#     rows = [row for row in comments_data]
#     # Convert the list of rows to a pandas DataFrame
#     data = pd.DataFrame(rows[1:], columns=rows[0])

# except Exception as e:
#     print('ERROR IN THE read_csv')


    # Convert the list of rows to a pandas DataFrame
#     data = pd.DataFrame(rows[1:], columns=rows[0])
# print(comments_data.head())
