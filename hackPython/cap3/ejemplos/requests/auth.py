import requests
import base64

from  requests.auth import HTTPDigestAuth

def pruebaBasic(user, password, protectedUrl):

    encoded = base64.encodestring(user + ':' + password)

    response = requests.get(protectedUrl, auth=(user, password))


def pruebaDigest(user, password, protectedUrl):
    
    response = requests.get(protectedUrl, auth=HTTPDigestAuth(user, password))