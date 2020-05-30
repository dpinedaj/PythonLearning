import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from checkWeb import MyWebPage


myweb = MyWebPage('http://wordpress.com')
print(myweb.check_built())