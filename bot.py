  
import tweepy

from getquote import get_quote

INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    quote = get_quote()
    api.update_status(quote)
    time.sleep(INTERVAL)