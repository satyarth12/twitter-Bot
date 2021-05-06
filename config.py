import tweepy
import logging
import os


logger = logging.getLogger()

def create_api():
	CONSUMER_KEY = 'TsvYuRil2MLiUqbmTYUyfRyln'
	CONSUMER_SECRET = 'OUks0XtSG0sPiVy6h2wY2zKPeKEzCb5yqDUb4W4f5fH5fm6L9e'
	ACCESS_KEY = '964632632482062337-AmlBZHGb1uTHT6A9jB5EqDJ4MHGIhnn'
	ACCESS_SECRET = 'eYOHt5tP80hXdSJxDsjTDtc7Y4uhSZS5dCu0UM4zFNZ7w'

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	'''
	Passing wait_on_rate_limit and wait_on_rate_limit_notify in the creation of the tweepy.
	API object makes Tweepy wait and print a message when the rate limit is exceeded.
	'''
	api = tweepy.API(auth,wait_on_rate_limit=True, 
       	 			wait_on_rate_limit_notify=True)


	try:
		api.verify_credentials()
	except Exception as e:
		logger.error("Error creating API", exc_info=True)
		raise e
	logger.info("API created")
	return api
