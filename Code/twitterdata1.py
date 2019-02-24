from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key="GQKQR3niOZpZx1yUZF7IEznrt"
consumer_secret="ZZQR9K8JewcgFMi0QKltCnZWXmndBWr47LUkNT9cESNJE8Rx6J "
access_token="1039581202645229568-XaKBBsig0noVjF1TfZ1F3FPRHKCQt9 "
access_secret="PJBPRziMAtcgHvEhUcycNU6ksdSnFOiHVIknhAkejULcR"
class StdOutListener(StreamListener):
 def on_data(self, data):
   print data
   return;
	
 def on_error(self,status):
  print (status)

if __name__  == ' __main__':
		
 listener = StdOutListener()
 auth = OAuthHandler(consumer_key,consumer_secret)
 auth.set_access_token(access_token,access_secret)
 stream = Stream(auth,listener)
 stream.filter(track=['donald trump'])