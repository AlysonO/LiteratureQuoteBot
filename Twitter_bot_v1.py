import tweepy, time
from Codes import *

'''So, i don't know what I am doing, let's hope it works'''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open('QUOTES.txt','r', encoding='utf8')
tweettext = filename.readlines()
filename.close()

for line in tweettext[0:100]:
    api.update_status(line)
    print(line)
    time.sleep(86400) # Sleep for 1 day

print("All done!")