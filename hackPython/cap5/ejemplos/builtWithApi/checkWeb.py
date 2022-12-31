import builtwith


class MyWebPage:
    def __init__(self, url):
        self.url = url

    def check_built(self):
        return builtwith.parse(self.url)
