import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("tweepy")

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

api_key = 'IhUrdm4yiGDzAn8a8p3OPmcKD'
api_secret_key = '9Z8h5trM19W0HDigcSEquP5sjk3acGVQhjTZw97B61tABeeMBR'
access_token = '4658837723-vPxtPeViNIW1AEsUNQX8M6rNE1pKlPBtLhpJLGH'
access_secret = 'tQN946Nv8NkGUrkhm2SkduTcs7V70ogsedFvlIpGluKET'


class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print(msg)
          #print(msg['text'].encode('utf-8'))
          self.client_socket.send( msg['text'].encode('utf-8'))
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
  auth = OAuthHandler(api_key, api_secret_key)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket))
  twitter_stream.filter(track=['uribe'])

if __name__ == "__main__":
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
        host = "127.0.0.1"     # Get local machine name
        port = 5555                # Reserve a port for your service.
        s.bind((host, port))        # Bind to the port

        print("Listening on port: %s" % str(port))

        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()        # Establish connection with client.

        print("Received request from: " + str(addr))

        sendData(c)
    finally:
        s.close()



