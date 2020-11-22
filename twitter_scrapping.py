#importing library
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import json
import pandas as pd
import csv
import re
from textblob import TextBlob
import string

import os
import time


# Twitter credentials
# Obtain them from your twitter developer account
consumer_key = 'Enter your consumer key'
consumer_secret = 'Enter your consumer_secret key'
access_token = 'Enter your access_token key'
access_token_secret = 'Enter your access_token_secret key'
# Pass your twitter credentials to tweepy via its OAuthHandler
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

/* */
def scraptweets(search_words, date_since, numTweets, numRuns):

    db_tweets = pd.DataFrame(columns = ['username', 'acctdesc', 'location', 'following',
                                        'followers', 'totaltweets', 'usercreatedts', 'tweetcreatedts',
                                        'retweetcount', 'text', 'hashtags']
                                )
    program_start = time.time()
    for i in range(0, numRuns):
        start_run = time.time()
        tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since, tweet_mode='extended').items(numTweets)
        tweet_list = [tweet for tweet in tweets]
        noTweets = 0
for tweet in tweet_list:
            username = tweet.user.screen_name
            acctdesc = tweet.user.description
            location = tweet.user.location
            following = tweet.user.friends_count
            followers = tweet.user.followers_count
            totaltweets = tweet.user.statuses_count
            usercreatedts = tweet.user.created_at
            tweetcreatedts = tweet.created_at
            retweetcount = tweet.retweet_count
            hashtags = tweet.entities['hashtags']
try:
            text = tweet.retweeted_status.full_text
except AttributeError:  
            text = tweet.full_text
            ith_tweet = [username, acctdesc, location, following, followers, totaltweets,usercreatedts, tweetcreatedts, retweetcount, text, hashtags]
            db_tweets.loc[len(db_tweets)] = ith_tweet  
            noTweets += 1
            end_run = time.time()
            duration_run = round((end_run-start_run)/60, 2)
        
            print('no. of tweets scraped for run {} is {}'.format(i + 1, noTweets))
            print('time take for {} run to complete is {} mins'.format(i+1, duration_run))
        
            time.sleep(920) #15 minute sleep time
from datetime import datetime
to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
path = os.getcwd()
filename = path + '/data/' + to_csv_timestamp + 'data.csv'
db_tweets.to_csv(filename, index = False)
    
program_end = time.time()
print('Scraping has completed!')
print('Total time taken to scrap is {} minutes.'.format(round(program_end - program_start)/60, 2))
    
    
# Initialise these variables:
search_words = "#popular"
date_since = "2019-10-10"
numTweets = 1000
numRuns = 6
# Call the function scraptweets
scraptweets(search_words, date_since, numTweets, numRuns)

