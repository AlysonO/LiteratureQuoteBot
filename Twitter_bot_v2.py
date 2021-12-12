from urllib.parse import quote
import tweepy, random
from datetime import time
from Codes import *

'''this one should work'''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot does

filename = open('QUOTES.txt','r', encoding='utf-8')
tweettext = filename.readlines()
filename.close()

quote_nbr = random.randint(1, 100) # Picks a random integer

for line in tweettext[quote_nbr:quote_nbr+1]: # Selects the line in the text file
    api.update_status(line)
    print(line) 
