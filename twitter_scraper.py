#Twitter (Scraping Likes, Retweets and Replies for a particular username in a specified duration)

import snscrape.modules.twitter as sntwitter #scraping Virat Kohli's Twitter between 01-01-22 & 17-11-17
import pandas as pd

maxTweets = 30
contents=[]
like=[]
retweet=[]
reply=[]

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@imVkohli+since:2016-01-01 until:2020-11-17').get_items()):
    if i > maxTweets :
        break
    contents.append(tweet.content)
    like.append(tweet.likeCount)
    retweet.append(tweet.retweetCount)
    reply.append(tweet.replyCount)

df = pd.DataFrame({'Tweet':contents, 'Like':like, 'ReTweet':retweet, 'reply':reply})
print(df)