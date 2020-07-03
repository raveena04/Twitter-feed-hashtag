# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:32:15 2020

@author: Raveena
"""

import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'Enter your consumer_key'
consumer_secret = 'Enter your consumer_secret key'
access_token = 'Enter your access token'
access_token_secret = 'Enter your access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#popular",count=100,
                           lang="en",
                           since="2019-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])