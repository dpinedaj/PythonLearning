import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from getInfo import GetInfo

host = "NS1.GOOGLE.COM"
wh = GetInfo(host)


def get_names():
    wh.get_names()


get_names()
