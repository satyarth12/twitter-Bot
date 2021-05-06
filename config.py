import tweepy
import logging
import os


logger = logging.getLogger()

def create_api():
	CONSUMER_KEY = 'enter your Consumer API keys here'
	CONSUMER_SECRET = 'enter your Consumer API secret keys here'
	ACCESS_KEY = 'enter your access token Access here'
	ACCESS_SECRET = 'enter your Access token secret here'

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
