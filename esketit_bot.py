from credentials import *
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


while True:
    t_count = 1
    api.update_status("ESKETI{0} #lilpump".format('T' * t_count))
    t_count += 1
    sleep(3600)
