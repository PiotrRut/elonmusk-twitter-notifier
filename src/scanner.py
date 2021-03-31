import tweepy
from apiconfig import startup
from tweets import tweet_engine


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet_engine(status)


def main():
    # Connect to the Twitter API
    api = startup()
    elon_tweet_listener = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    # '44196397' is the ID for the @elonmusk account
    elon_tweet_listener.filter(follow=["44196397"], is_async=True)


if __name__ == "__main__":
    main()
