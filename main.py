import tweepy, time, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from ghost import Ghost
import random



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

follower_id_list = api.friends_ids()
follower_screen_name_list = []
public_tweets = api.home_timeline()
##for tweet in public_tweets:
    
    ##long_str = tweet.user.name + ": " + tweet.text
    ##print (long_str)
    ##print("\n")

##Debugging
count = 0
if count<5:
    for userID in follower_id_list:
        follower_string = "https://twitter.com/" + api.get_user(userID).screen_name
        follower_screen_name_list.append(follower_string)
        count = count + 1

print(follower_screen_name_list)
##Debugging - Replace with an inquiry
#test = follower_id_list[0]
#testList = api.friends_ids(test)
#for i in range(5):
#    print(api.get_user(testList[i]).screen_name)
    
g = Ghost()
with g.start() as session:
    for i in range(len(follower_screen_name_list)):
        testStr = "" + i
        page, extra_resources = session.open(follower_screen_name_list[i])
        session.capture_to("test" + testStr +".png")
    
