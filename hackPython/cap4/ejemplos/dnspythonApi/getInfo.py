import dns
from dns import resolver, name


class GetInfo:
    def __init__(self, domain):
        self.domain = domain

    def query(self, dType):
        result = resolver.query(self.domain, dType)
        print(result.response.to_text())
