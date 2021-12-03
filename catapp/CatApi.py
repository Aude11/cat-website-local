import requests
from .ImageApi import ImageApi


class CatApi(ImageApi):
    def __init__(self):
        self.url = "https://api.thecatapi.com/v1/images/search"
        self.api_key = "581a4b3d-7fbb-445b-bac1-fb8af477744f"
        self.headers = {'x-api-key': self.api_key}

    def _get_request(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def _get_content(self):
        response = self._get_request()
        if type(response) == list:
            if len(response) != 0:
                return response[0]
            return None
        return None

    def get_url_image(self):
        data = self._get_content()
        if data is not None:
            return data["url"]
        else:
            return None
