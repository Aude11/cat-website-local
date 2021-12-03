from flask import Flask, render_template, Response, request, redirect, url_for
from flask.views import View
import datetime
from .HandleUserRequest import HandleUserRequest
from .ViewIndex import app
from .Pagination import Pagination


class ViewArchive(View):

    methods = ['GET', 'POST']

    def __init__(self, controller, maximun_item_per_page, pagination):
        self.controller = controller
        self.maximun_item_per_page = maximun_item_per_page
        self.pagination = pagination
        self.year = datetime.datetime.now().year

    def _notify_update_item_like(self, result):
        self.controller.update_likes(result)

    def _notify_get_all_items(self):
        all_items = self.controller.get_cats()
        return all_items

    def _notify_get_count_items(self):
        number_items_in_data_base = self.controller.count_items_data_base()
        return number_items_in_data_base

    def _get_limit(self, page, number_of_total_pages, number_items):  # should be in pagniation ??
        offset = self.pagination.get_offset(page) 
        remain = self.pagination.get_remain(number_items)
        if (page == number_of_total_pages) & (remain != 0):
            limit = offset + remain
        else:
            limit = offset + self.maximun_item_per_page
        return limit

    def _get_total_pages(self, page, number_items):
        number_of_total_pages = self.pagination.get_total_pages(page,
                                                                number_items)
        return number_of_total_pages

    def dispatch_request(self, page):
        current_year = self.year
        if page:
            if request.method == 'POST':
                result = request.form
                self._notify_update_item_like(result)
                return redirect(url_for('archive', page=page))
            number_items = self._notify_get_count_items()
            number_of_total_pages = self._get_total_pages(page, number_items)
            if number_of_total_pages is None:
                return redirect(url_for('index'))
            else:
                next_page = self.pagination.get_next_page(page, number_items)
                previous_page = self.pagination.get_previous_page(page)
                offset = self.pagination.get_offset(page)
                limit = self._get_limit(page, number_of_total_pages,
                                        number_items)
                cats = self._notify_get_all_items()
                return render_template('archive.html', year_test=current_year,
                                       cats=cats,
                                       starting=offset, end=limit, page=page,
                                       next_page=next_page,
                                       previous_page=previous_page,
                                       number_of_total_pages=number_of_total_pages)
        else:
            return redirect(url_for('index'))
