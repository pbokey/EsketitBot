import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
                 
if __name__ == '__main__':
    while True:
        t_count = 3
        api.update_status("ESKETI{0} #lilpump".format('T' * t_count))
        t_count += 1
        sleep(3600)
