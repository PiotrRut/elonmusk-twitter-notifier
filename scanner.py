import tweepy
import time
from apiconfig import startup
from emailsender import send_mail


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if any(tweet in status.text for tweet in ['stock', 'share', '$', 'doge']):
            # send e-mail
            send_mail(f"Elon tweeted: {status.text}")


def main():
    # connect to the Twitter API
    api = startup()
    elon_tweet_listener = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    # '44196397' is the ID for the @elonmusk account
    elon_tweet_listener.filter(follow=['1499189731'], is_async=True)


if __name__ == "__main__":
    main()


