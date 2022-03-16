import scrapy

class Scrapper:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.data = None

    def get_response(self):
        self.response = scrapy.Request(self.url)
        return self.response

    def get_data(self):
        self.data = self.response.text
        return self.data
    