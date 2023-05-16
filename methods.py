import pandas as pd
import csv

# this works but result is list of list
'''
>>>
    [
    ['XpVt6Z1Gjjo', "Logan Paul it's yo big day ‼️‼️‼️", '4', '0'],
    ['XpVt6Z1Gjjo', 'Say hi to Kong and maverick for me', '3', '0']
    ]
'''
def us_comments():
    with open('data/UScomments.csv', mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile, quoting=csv.QUOTE_ALL)
        header_data = list(next(reader))
        infile = infile.read().replace('\0', '').splitlines()
        comment_data = list(csv.reader(infile))
    #print(comment_data[963])
    #return comment_data[963][1]
    #print(comment_data[:5])
    return comment_data


# to read count csv, should maintain usecols becasue commas are inside string, otherwise will crash
# i included to_csv to save the clipped data that works for us
def us_videos():
    count_data = pd.read_csv('data/USvideos.csv', usecols=['video_id','title','views','likes','dislikes','comment_total'])
    
    # return (count_data.iloc[963])
    return count_data



def process_comment_data(comment_data):
    '''
    process_comment_data()
    returns a list of unique video ids along with their comment count
    '''
    list_of_ids = []
    comment_map = {}
    for comment in comment_data:
        # Append the video ID to the list_of_ids
        list_of_ids.append(comment[0])

        # Update the comment_map with the count of comments for each video ID
        if comment[0] not in comment_map:
            comment_map[comment[0]] = 1
        else:
            comment_map[comment[0]] += 1
    # print(len(list_of_ids))
    # print(len(list(set(list_of_ids))))
    # print(len(comment_map))
    # for key in comment_map:
    #     print(key, comment_map[key])
    return list_of_ids, comment_map


def agregate_sentiments(comment_map, polarity_score_list):

    '''
    this function average score calculator for a video and a send it to a csv.

    Args:
        comment_map (hashMap(str, int)): has unique video_id and count of it
        polarity_score_list(list of int): list of sentiment polarity score

    Returns: 
        writes out a csv file=>
            video_id,compound_score
            zuKX0fPlo2Q,0.9394
            UJKl7ToDi20,0.8954999999999999
            dsH83p_mfEs,0.8493666666666666
    '''
    score_agregate = {}
    #calulating sum of scores for a video
    for comment in polarity_score_list:
        vid_id = comment[0]
        if vid_id not in score_agregate:
            score_agregate[vid_id] = comment[2]
        else:
            score_agregate[vid_id] += comment[2]
    
    # at this point the agregate value contains sums for each video
    for vid_id in score_agregate:
        score_agregate[vid_id] /= comment_map[vid_id]
    
    # write the csv in descending order
    top_items = sorted(score_agregate.items(), key=lambda x: x[1], reverse=True)

    # write the items to a CSV file
    with open('top_items.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['video_id', 'compound_score'])
        for key, value in top_items:
            writer.writerow([key, value])


def merger():

    count_data = pd.read_csv('data/USvideos.csv', usecols=['video_id','title','views','likes','dislikes','comment_total'], index_col=None)
    #print('count_data: ', type(count_data))
    # Read the score CSV file
    score_csv = pd.read_csv('top_items.csv', index_col=None)
    #print('score_csv: ', type(score_csv))
        
    # Merge the two dataframes on 'video_id' column
    merged_df = pd.merge(count_data, score_csv, on='video_id')

    # drop duplicates based on a specific column (e.g. 'column_name')
    merged_df.drop_duplicates(subset=['video_id'], inplace=True)

    # Save the merged dataframe as CSV
    merged_df.to_csv('merged.csv', index=False)
    