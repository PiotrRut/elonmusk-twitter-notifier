# Stonks Twitter Scanner

This little scripts uses the `tweepy` Python library, which is a wrapper around the Twitter API.
It sets up a listener on the [@elonmusk](https://twitter.com/elonmusk) Twitter account, and automatically detects whenever Elon Musk posts a tweet mentioning the keywords `share`, `stock`, `doge`, and `$`, or any words
that contain any of those strings as substrings.

When a new tweet that meets the conditions is read, this program will automatically e-mail me with the transcript of that tweet. This is a way for me
to always be up to date with stocks that may soon rise in value 🤡

It is hosted on a Heroku dyno and is set to never sleep in order to provide as accurate service as possible.

## Usage and config
If you would like to use this yourself, and receive juicy e-mail notifications every time
Elon tweets, you can too! All you have to do is to have a [Twitter Developer account](https://developer.twitter.com/en) and update the following environmental variables with your
Twitter API access keys:

```python
# ./src/apiconfig.py

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_SECRET')
```

You will also have to update the following with your own e-mail details:

```python
# ./src/emailsender.py

mail_from = os.getenv('EMAIL_FROM')
mail_to = os.getenv('EMAIL_TO')
mail_pw = os.getenv('EMAIL_PW')
```
**You might also have to update the SMTP server and port if you're not using Gmail.**

## Upcoming features

In the feature I (hopefully) would like to integrate this with Amazon SNS which would send
me a text message instead of an e-mail, however the current solution is the
most cost effective one and sufficient for now.

---
_may the stonks be ever in your favour_