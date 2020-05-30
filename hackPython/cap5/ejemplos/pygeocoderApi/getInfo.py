from pygeocoder import Geocoder

class MyGeoCoder:
    @staticmethod
    def get_geocode():
        return Geocoder.geocode("Mountain View")