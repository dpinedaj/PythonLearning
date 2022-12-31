import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pentest import FunTester

fn = FunTester()
print(fn.logins)
