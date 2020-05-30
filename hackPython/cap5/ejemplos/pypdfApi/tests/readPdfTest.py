import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pdfReader import MyPdfReader

myreader = MyPdfReader("../files/Understanding Cryptography-Christof Paar, Jan Pelzl.pdf")
myreader.print_info()
myreader.extract_images("../files/images")
