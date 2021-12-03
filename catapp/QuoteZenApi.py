import requests
from .QuoteApi import QuoteApi

class QuoteZenApi(QuoteApi):
    def __init__(self):
        self.url = "https://zenquotes.io/api/random"

    def _get_request(self):
        response = requests.request("GET", self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_content(self):
        response = self._get_request()
        if type(response) == list:
            if len(response) != 0 :
                return response[0]
            return None
        return None

    def get_quote(self):
        content_quote = self.get_content()
        if content_quote is not None:
            return content_quote["q"]
        else:
            return None

    def get_author(self):
        content_quote = self.get_content()
        if content_quote is not None:
            return content_quote["a"]
        else:
            return None
