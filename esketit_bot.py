import tweepy
from time import sleep

consumer_key = 'rihI6V6y8dMviBKwp38zaAfhb'
consumer_secret = 'e0P2dCEpFwbRH86BlnjSuPULNpwtMLkNVzUia61dUiH4elgMGb'
access_token = '961825486199406592-kKGL6eqVK4knN6BciPbCkqXPfCPqipk'
access_token_secret = 'oNfrJORH0dYw92il8aJ2QDGGnVCNuJaVWXAHVAgy6DJON'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth
                 
if __name__ == '__main__':
    while True:
        t_count = 3
        api.update_status("ESKETI{0} #lilpump".format('T' * t_count))
        t_count += 1
        sleep(3600)
