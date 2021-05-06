import tweepy
import logging
from config import create_api
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


'''
Reply back to the mentions with a specific keyword
'''


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return



def reply_to_tweets(api):
	last_seen_id = retrieve_last_seen_id(FILE_NAME)

	mentions = api.mentions_timeline(last_seen_id, #since_id :  Returns only statuses with an ID greater than the specified ID.
					tweet_mode = "extended")


	for mention in reversed(mentions): #responding to the old tweets first
		print(str(mention.id) + "-" + mention.full_text)
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)

		if "#helloworld" in mention.full_text.lower():
			# if not tweet.user.following:
   #              tweet.user.follow()

			logger.info(f"Answering to {tweet.user.name}")
			api.update_status('@' + mention.user.screen_name +
	                    '#HelloWorld back to you!. This is just a test.', mention.id)





def main():
	api = create_api()
	while True:
		reply_to_tweets(api)
		logger.info("Waiting...")
		time.sleep(15)



if __name__ == "__main__":
    main()