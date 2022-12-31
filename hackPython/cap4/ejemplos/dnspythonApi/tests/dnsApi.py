import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from getInfo import GetInfo


gi = GetInfo("www.google.com")
gi.query("A")
