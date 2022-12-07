## Scrape data from twitter with Snscrape and store in csv files <keyword>.csv
from calendar import month_name
from random import getrandbits
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime
import os



def CheckLeap(Year):  
    if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
        return 366
    else:  
        return 365

def getData(keyword,year):
    tweets_list = []

    if CheckLeap(year) == 365:
        days = list(range(1,366))
    else:
        days = list(range(1,367)) 

    for day_num in days:
        date_since= datetime.strptime(str(year) + "-" + str(day_num), "%Y-%j").strftime("%Y-%m-%d")
    
        if(day_num == len(days)):
            date_until= datetime.strptime(str(year+1) + "-" + str(1), "%Y-%j").strftime("%Y-%m-%d")
        else:
            date_until= datetime.strptime(str(year) + "-" + str(day_num+1), "%Y-%j").strftime("%Y-%m-%d")

        for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'${keyword} since:{date_since} until:{date_until}').get_items()):
            # sets the number of tweets to be collected per day (upper bound)
            if i>99:
                break
            tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.user.verified, tweet.user.followersCount, tweet.user.location,tweet.replyCount, tweet.retweetCount, tweet.likeCount,tweet.media])
        
        # Creating a dataframe from the tweets list above
        print(date_since, len(tweets_list))
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username','Verified Status','Follower Count','Location','Reply Counts','Retweet Counts','Like Count','Media'])

    return tweets_df

# keywords to pull tweets with
keywords = ['climatehoax',...]
# years to pull tweets from 
years = [2018,2019,2020,2021]

for k in keywords:
    for y in years:
        
        df = getData(k,y)
        # PATH to store the data
        path = '/Users/padmaprabagaran/dev/Pro-Change-Capstone/data/' 
        if not os.path.exists(path):
            os.makedirs(path)

        df.to_csv(path+f'{k}_{y}.csv',index=False)




