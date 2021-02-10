import tweepy
import time
from apiconfig import startup


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if any(tweet in status.text for tweet in ['stock', 'share', '$', 'doge']):
            print('ELON MUSK TWEETED:', status.text)
            print('AT', time.ctime(), '\n')


def main():
    api = startup()
    elon_tweet_listener = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    # '44196397' is the ID for the @elonmusk account
    elon_tweet_listener.filter(follow=['1499189731'], is_async=True)


if __name__ == "__main__":
    main()


