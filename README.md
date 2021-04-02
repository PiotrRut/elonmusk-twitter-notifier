# Stonks Twitter Scanner 📈

<img src="https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue" />

This little scripts uses the [tweepy](https://www.tweepy.org/) Python library, which is a wrapper around the Twitter API.
It sets up a listener on the [@elonmusk](https://twitter.com/elonmusk) Twitter account, and automatically detects whenever Elon Musk posts a tweet mentioning the any of the specified keywords
(or any words containing those as substrings). 

It also uses AI object detection from images using a [YOLO](https://pjreddie.com/darknet/yolo/) based model that I've custom-trained to detect
objects such as dogecoins, bitcoins, doge etc.. in the images.

When a new tweet that meets the conditions is read, this program will automatically e-mail me with the transcript of that tweet. For tweets containing an image that the AI
classifies as ones containing objects it's trained to detect, the image will be attached as well. This is a way for me
to always be up to date with stocks that may soon rise in value 🤡

## Prerequisites 🗂

In order to run this locally, make sure you're Python interpreter is between v3.6 and 3.8 - 
this is due to the fact that Tensorflow won't work with newer versions. If you're on a newer
Python version, consider downgrading with [pyenv](https://github.com/pyenv/pyenv).

To install all the necessary dependencies, simply run the following command inside project root 👇🏻

```bash
$ pip install -r requirements.txt
```

Note:
I have *not* included my trained AI model in the repository due to the large file size - 
you can get it by navigating to the [releases](https://github.com/PiotrRut/elonmusk-twitter-notifier/releases) tab, downloading `doge-ai.h5` and placing it in the root
of the project.

## Usage and config 👨🏻‍💻

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
You might also have to update the SMTP server and port if you're not using Gmail.

## Deployment 🚀

Unless you want to keep this program running inside an open terminal instance forever, you should think about
deploying it somewhere. To do this, first find a platform that suits your needs, such as Heroku, Amazon AWS or MS Azure.

You need to remember to set the same config vars on the server as you've done locally, otherwise
the program won't work. You also need to make sure that you install all the necessary dependencies (tweepy) - for most platforms this is done
by specifying them inside the `requirements.txt` file, but some services might need more. You will also have to make sure that your platform does not use Python above v3.8!

Some platforms also charge differently and offer different types of containers, so make sure you find one that suits your needs and dones't cost much.

### Dealing with bundle size 📦
One thing to keep in mind is that because of the large size of the AI model, as well as the size of the tensorflow install, the overall bundle size gets quite big quite quickly. Some platforms
(particularly Heroku) limit the bundle size you can deploy (for Heroku it's 500mb), and thus deployment can become troublesome.

## Preview 📲

<details>
  <summary><i><b>Reveal screenshots</b></i></summary>
  <p>

| Notification | Image attachment |
| ----------- | ----------- |
| ![image](https://user-images.githubusercontent.com/43642399/113286944-c62d7a00-92e4-11eb-9a78-1f64b43f13df.png) | ![image](https://user-images.githubusercontent.com/43642399/113286990-d9404a00-92e4-11eb-9dd9-be259d80ef7b.png) |

  </p>
</details>


---
_may the stonks be ever in your favour_
