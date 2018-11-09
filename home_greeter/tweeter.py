import tweepy

class Tweeter():
    def __init__(self, api=None):
        self.__api = api or self.__api()

    def tweet_image(self, image):
        tweet = 'tweet'
        status = self.__api.update_with_media(image, tweet)
        self.__api.update_status(status = tweet)

    def __api(self):
        consumer_key = 'ck'
        consumer_secret = 'cs'
        access_token = 'at'
        access_token_secret = 'ast'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
