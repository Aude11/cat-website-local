from flask import Flask, render_template, Response, request, redirect, url_for
from flask.views import View
import datetime
import time 
from .HandleUserRequest import HandleUserRequest


app = Flask(__name__)

class ViewIndex(View):
    methods = ['GET', 'POST']

    def __init__(self, controller):
        self.controller = controller
        self.year = datetime.datetime.now().year

    def _notify_update_item_like(self, result):
        self.controller.update_likes(result)

    def _notify_get_last_item_added(self):
        last_item_added = self.controller.get_last_cat()
        if last_item_added is not None:
            return last_item_added
        else:
            return self._get_backup_item()

    def _get_backup_item(self):
        backup_item = {'date': datetime.datetime.now(), 'url': 'url',
                        'quote': 'quote', 'author': 'author', 'likes': 0}
        return backup_item

    def dispatch_request(self, is_caturday=False, btn_click=False):
        cat = self.controller.get_last_cat()
        current_year = self.year
        if request.method == 'POST':
            result = request.form
            for key, value in result.items():
                    x = key
            self._notify_update_item_like(result)
            return redirect(url_for('index'))
        else:
            return render_template('index.html',
                                   current_year=current_year,
                                   cat=cat, is_caturday=is_caturday,
                                   btn_click=btn_click)
