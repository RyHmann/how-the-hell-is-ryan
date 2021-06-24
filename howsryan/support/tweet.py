import requests
import config
from datetime import datetime


class Tweet:
    def __init__(self):
        self.url = "https://api.twitter.com/2/users/1250237559826829313/tweets?expansions=attachments" \
                           ".media_keys&tweet.fields=created_at,attachments&media.fields=url,preview_image_url"
        self.headers = {
            'Authorization': 'Bearer ' + config.twit_bearer_token
        }
        self.twitter_data = requests.request("GET", self.url, headers=self.headers).json()
        self.recent_tweet = self.get_tweet(self.twitter_data)
        self.tweet_media = self.get_tweet_pic(self.twitter_data)
        self.tweet_text = self.get_tweet_text(self.recent_tweet)
        self.tweet_created = self.get_tweet_created(self.recent_tweet)
        self.media_key = self.get_media_key(self.recent_tweet)
        self.tweet_img_url = self.get_img_url(self.media_key)
        self.tweet_url = self.get_tweet_url(self.recent_tweet)

    def get_tweet(self, tweet):
        #returns dictionary with keys: attachments, text, created_at, id
        #attachments is a dictionary with key: media_keys
        return tweet["data"][0]

    def get_tweet_pic(self, tweet):
        #returns dictionary with keys: media_key, type, url
        media = tweet["includes"]["media"][0]
        return media

    def get_tweet_text(self, tweet):
        tweet_word_list = tweet["text"].split(" ")[:-1]
        tweet_text = " ".join(tweet_word_list)
        return tweet_text

    def get_tweet_created(self, tweet):
        time_created = tweet["created_at"][:10]
        datetime_created = datetime.strptime(time_created, "%Y-%m-%d")
        formatted_time_string = datetime.strftime(datetime_created, "%b %d")
        return formatted_time_string

    def get_media_key(self, tweet):
        return tweet["attachments"]["media_keys"]

    def get_img_url(self, media_key):
        if media_key[0] == self.tweet_media["media_key"]:
            return self.tweet_media["url"]

    def get_tweet_url(self, tweet):
        return tweet["text"].split(" ")[-1]
