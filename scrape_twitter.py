## Scrape data from twitter with Snscrape and store in csv files <keyword>.csv
import snscrape.modules.twitter as sntwitter
import pandas as pd

keywords = ['climatechange','globalwarming','extremeweather','heatwave','carbonemissions','sustainable','emissions','climatescience','carbonneutral','ClimateCrisis','ClimateEmergency','ClimateScam']


# Created a list to append all tweet attributes(data)
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for x in keywords:
    print(x)

    # 2021
    for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'${x} since:2021-01-01 until:2021-12-31').get_items()):
        if i>3000:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.user.verified, tweet.user.followersCount, tweet.user.location,tweet.replyCount, tweet.retweetCount, tweet.likeCount,tweet.media])
        
    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username','Verified Status','Follower Count','Location','Reply Counts','Retweet Counts','Like Count','Media'])

    print('2021:'+str(len(tweets_df)))
    tweets_df.to_csv(f'data/{x}/{x}_2021.csv',index=False)

    tweets_list = []

    # ------------------------------------------------------
    # 2022

    for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'${x} since:2022-01-01 until:2022-09-05').get_items()):
        if i>3000:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.user.verified, tweet.user.followersCount, tweet.user.location,tweet.replyCount, tweet.retweetCount, tweet.likeCount,tweet.media])
        
    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username','Verified Status','Follower Count','Location','Reply Counts','Retweet Counts','Like Count','Media'])

    print('2022:'+str(len(tweets_df)))
    tweets_df.to_csv(f'data/{x}/{x}_2022.csv',index=False)

    tweets_list = []

    # ------------------------------------------------------
    # 2020
    for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'${x} since:2020-01-01 until:2020-12-31').get_items()):
        if i>3000:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.user.verified, tweet.user.followersCount, tweet.user.location,tweet.replyCount, tweet.retweetCount, tweet.likeCount,tweet.media])
        
    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username','Verified Status','Follower Count','Location','Reply Counts','Retweet Counts','Like Count','Media'])

    print('2020:'+str(len(tweets_df)))
    tweets_df.to_csv(f'data/{x}/{x}_2020.csv',index=False)

    tweets_list = []

    # 2019
    for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'${x} since:2019-01-01 until:2019-12-31').get_items()):
        if i>3000:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.user.verified, tweet.user.followersCount, tweet.user.location,tweet.replyCount, tweet.retweetCount, tweet.likeCount,tweet.media])
        
    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username','Verified Status','Follower Count','Location','Reply Counts','Retweet Counts','Like Count','Media'])

    print('2019:'+str(len(tweets_df)))
    tweets_df.to_csv(f'data/{x}/{x}_2019.csv',index=False)
