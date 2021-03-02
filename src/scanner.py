import tweepy
from apiconfig import startup
from emailsender import send_mail
import time


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        keywords = ['stock', 'share', '$', 'doge', 'crypto', 'bitcoin']
        # this solution will exclude replies and mentions and only return Elon's tweets
        if any(tweet in status.text.lower() for tweet in keywords) and status.user.id_str == '44196397':
            # send e-mail
            send_mail(f"Elon tweeted: {status.text.encode('UTF-8')} - on {time.ctime()}")


def main():
    # connect to the Twitter API
    api = startup()
    elon_tweet_listener = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    # '44196397' is the ID for the @elonmusk account
    elon_tweet_listener.filter(follow=['44196397'], is_async=True)


if __name__ == "__main__":
    main()
