# web_app/services/twitter_service.py

import tweepy
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

#class TwitterService():
#    def __init__(self):
#        self.auth = _________
#        self.api = _________
#
#service = TwitterService()
#service.api.get_user("_______")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", auth)

api = tweepy.API(auth)
print("API", api)
#print(dir(api))

if __name__ == "__main__":

    screen_name = input("Please input a twitter screen name (e.g. s2t2): ")

    #
    # how to get information about a given twitter user?
    #

    user = api.get_user(screen_name)
    #> <class 'tweepy.models.User'>

    #pprint(user._json)
    print(user.id)
    print(user.screen_name)
    print(user.friends_count)
    print(user.followers_count)

    #
    # how to get tweets from a given twitter user?
    #

    #statuses = api.user_timeline("s2t2")
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    #status = statuses[0]
    #pprint(dir(status))
    #pprint(status._json)
    #print(status.id)
    #print(status.full_text)

    for status in statuses:
        print("----")
        print(status.full_text)
