
import csv

comments = []

def make_csv(comments):
    header = comments[0].keys()
    
    # if channelID:
    #     filename = f'comments_{channelID}.csv'
    # else:
    #     filename= f'comments_no_name.csv'
    filename= f'comments_video_comments.csv'
    with open(filename, 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(comments)



def process_comments(response_items):

    for res in response_items:

        # loop through the replies
        if 'replies' in res.keys():
            for reply in res['replies']['comments']:
                comment = reply['snippet']
                comment['commentId'] = reply['id']
                comments.append(comment)
        else:
            comment = {}
            
            comment['snippet'] = res['snippet']['topLevelComment']['snippet']
            comment['snippet']['parentId'] = None
            comment['snippet']['commentId'] = res['snippet']['topLevelComment']['id']

            comments.append(comment['snippet'])
            

    make_csv(comments)
    
    print(f'Finished processing {len(comments)} comments.')
    return comments