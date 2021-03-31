import tweepy
import logging
import os

logger = logging.getLogger()


def startup():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    try:
        api.verify_credentials()
    except tweepy.TweepError as e:
        logger.error("Check credentials!!!", exc_info=True)
        raise e
    logger.info("Started")
    return api
