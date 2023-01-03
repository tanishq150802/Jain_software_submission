from facebook_scraper import get_posts
import pandas as pd
post_cap=[]
like=[]
com=[]
share=[]
for post in get_posts('nintendo', pages=4):
    post_cap.append(post['text'])
    like.append(post['likes'])
    com.append(post['comments'])
    share.append(post['shares'])

df = pd.DataFrame({'Text':post_cap, 'Like':like, 'Comments':com, 'shares':share})
print(df.head())