import datetime


class DatesManager:
    def __init__(self, date=datetime.datetime.now()):
        self.date = date

    def get_month(self):
        return self.date.strftime("%B")

    def get_day(self):
        return self.date.strftime("%A")

    def get_year(self):
        return self.date.year

    def get_date_short(self):
        return self.date.strftime("%x")
