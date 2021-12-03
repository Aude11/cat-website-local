from flask import Flask, render_template, Response, request, redirect, url_for
from flask.views import View
import datetime
import time
from .HandleUserRequest import HandleUserRequest
from .ViewIndex import app

class ViewUpdateImage(View):
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

    def _notify_create_new_item(self):
        self.controller.add_new_item_in_data_base()

    def _get_backup_item(self):
        backup_item = {'date': datetime.datetime.now(),
                       'url': 'url', 'quote': 'quote',
                       'author': 'author', 'likes': 0}
        return backup_item

    def dispatch_request(self):
        current_year = self.year
        btn_click = True
        current_day = datetime.datetime.now().strftime("%A")
        if current_day == 'Saturday':
            is_caturday = True
            self._notify_create_new_item()
        else:
            is_caturday = False
        cat = self._notify_get_last_item_added()
        return render_template('index.html', current_year=current_year,
                               cat=cat,
                               is_caturday=is_caturday, btn_click=btn_click)
