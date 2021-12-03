import datetime
from .CatApi import CatApi
from .QuoteZenApi import QuoteZenApi


class SchemaCaturday:
    def __init__(self, cat_api, quote_api):
        self.cat_api = cat_api
        self.quote_api = quote_api
        self.url = "url"
        self.date = "date"
        self.quote = "quote"
        self.author = "author"
        self.likes = "likes"

    def _check_input_data_type(self, url, quote, author):
        if type(url) != str:
            return False
        if type(quote) != str:
            return False
        if type(author) != str:
            return False
        return True

    def create_new_document(self):
        date = datetime.datetime.now()
        likes = 0
        url = self.cat_api.get_url_image()
        quote = self.quote_api.get_quote()
        author = self.quote_api.get_author()
        is_fields_correct = self._check_input_data_type(url, quote, author)
        if is_fields_correct is True:
            return {self.date: date, self.url: url,
                    self.quote: quote, self.author: author, self.likes: likes}
        else:
            return None
