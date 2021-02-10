# Stonks Twitter Scanner

This little scripts uses the `tweepy` Python library, which is a wrapper around the Twitter API.
It sets up a listener on the [@elonmusk](https://twitter.com/elonmusk) Twitter account, and automatically detects whenever Elon Musk posts a tweet mentioning the keywords `share`, `stock`, `doge`, and `$`, or any words
that contain any of those strings as substrings.

When a new tweet that meets the conditions is read, this program will automatically e-mail me with the transcript of that tweet. This is a way for me
to always be up to date with stocks that may soon rise in value 🤡

It is hosted on a Heroku dyno and is set to never sleep in order to provide as accurate service as possible.

## Upcoming features

In the feature I (hopefully) would like to integrate this with Amazon SNS which would send
me a text message instead of an e-mail, however the current solution is the
most cost effective one and sufficient for now.

---
_may the stonks be ever in your favour_