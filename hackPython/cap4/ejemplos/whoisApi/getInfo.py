import sys
import pythonwhois

class GetInfo:
    def __init__(self, host):
        self.host = host
    
    def get_names(self) -> None:
        whois = pythonwhois.get_whois(self.host)
        for key in whois.keys():
            print("{} : {}\n".format(key, whois[key]))

    def get_root_server(self) -> None:
        whois = pythonwhois.net.get_root_server(self.host)
        print(whois)

    def get_raw_server(self) -> None:
        whois = pythonwhois.net.get_whois_raw(self.host)
        print(whois)


