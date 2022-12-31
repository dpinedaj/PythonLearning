import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from getInfo import MyGeoCoder

results = MyGeoCoder.get_geocode()

print(results.coordinates)
print(results.country)
print(results.postal_code)
print(results.latitude)
print(results.longitude)
