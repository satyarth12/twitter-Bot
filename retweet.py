import tweepy
import logging
from config import create_api
import json
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


'''
Tweepy stream to actively watch for tweets that contain certain keywords. 
For each tweet, if you’re not the tweet author, it will mark the tweet as Liked and then retweet it.
'''

class RetweetListener(tweepy.StreamListener):

	def __init__(self, api):
		self.api = api
		self.me = api.me()


	def on_status(self, tweet):
		logger.info(f"Processing tweet id {tweet.id}")

		if tweet.in_reply_to_status_id is not None or \
			tweet.user.id == self.me.id:
			return 

		if not tweet.favorited:
			try:
				tweet.favorite()
			except Exception as e:
				logger.error("Error on favorite tweet", exc_info=True)

		if not tweet.retweeted:
			try:
				tweet.retweet()
			except Exception as e:
				logger.error("Error on favorite and retweet", exc_info=True)


	def on_error(self, status):
		logger.error(status)



def main(keywords):
	api = create_api()
	tweets_listener = RetweetListener(api)
	stream = tweepy.Stream(auth = api.auth, listener = tweets_listener)
	stream.filter(track=keywords, languages=["en"])	
	time.sleep(60)


if __name__ == "__main__":
    main(["Python", "Machine Learning"])