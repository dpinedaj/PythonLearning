import shodan
from constants import Constants as cts
class ShodanSearch:

    def __init__(self):
        self.cts = cts()
        self.api = shodan.Shodan(self.cts.APIKEY)

    def search(self, text):
        try:
            result = self.api.search(str(text))
            
        except Exception as exc:
            print('Error',str(exc))
            result = None
        
        return result

    def info_host(self, ip):
        try:
            result = self.api.host(ip)

        except Exception as exc:
            print('Error',str(exc))
            result = None

        return result
