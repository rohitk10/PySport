#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "725032356952850432-ezh11wNZSMITyfc30FAO1NT2QwGFznh"
access_token_secret = "ZKZi9YvKSUqdKGCOTJOhFKLK25LunbvH7pelKm8dVPNoz"
consumer_key = "Xz63VmymUDujXtqT3QyMfJDa1"
consumer_secret = "8JPWUA0FVW8W0Vh46L2hqgH4QtVyurgYF5XQ1Bf2DFllBwwpeC"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['madrid', 'MADRID', 'real madrid', 'hala madrid', 'HALA MADRID', 'REAL MADRID', 'mancity', 'MANCITY', 'man city', 'madrid vs city', 'MADRID VS CITY', 'real vs man city', 'los blancos', 'manchester', 'manchester city', 'MANCHESTER CITY', 'mcfc', 'MCFC', 'manchester city fc', 'MANCHESTER CITY FC', 'man city fc', 'MAN CITY FC'])
