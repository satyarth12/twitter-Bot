import tweepy
import logging
from config import create_api
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


'''
Follow back your followers
'''

def followFollowers(api):
	logger.info("Getting your followers and folowing them")

	for follower in tweepy.Cursor(api.followers).items():
		if not follower.following:
			logger.info(f"Following {follower.name}")
			follower.follow()


def main():
	api = create_api()
	while True:
		followFollowers(api)
		logger.info("Waiting for the data ... ")
		time.sleep(30)



if __name__ == "__main__":
    main()