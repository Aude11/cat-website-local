 # should it be handle by the controler??


class Pagination:
    def __init__(self, maximun_item_per_page):
        self.maximun_item_per_page = maximun_item_per_page

    def get_total_pages(self, page_asked, number_items):
        if number_items > self.maximun_item_per_page:
            factor = self.get_factor(number_items)
            remain = self.get_remain(number_items)
            if remain == 0:
                number_of_total_pages = factor
            else:
                number_of_total_pages = factor + 1
                if page_asked > number_of_total_pages:
                    return None
        else:
            number_of_total_pages = 1
            return number_of_total_pages
        return number_of_total_pages

    def get_factor(self, number_items):
        factor = number_items // self.maximun_item_per_page
        return factor

    def get_remain(self, number_items ):
        remain = number_items % self.maximun_item_per_page
        return remain

    def get_offset(self, page_asked):
        offset = (page_asked - 1) * self.maximun_item_per_page
        return offset

    def get_next_page(self, page_asked, number_items):
        number_of_total_pages = self.get_total_pages(page_asked, number_items)
        if page_asked == number_of_total_pages:
            return None
        else:
            nb_next = page_asked + 1
            return nb_next

    def get_previous_page(self, page_asked):
        if page_asked > 1:
            nb_previous = page_asked - 1
            return nb_previous
        else:
            return None

    def get_limit(self, page, number_items, maximun_item_per_page):
        offset = self.get_offset(page)
        remain = self.get_remain(number_items)
        number_of_total_pages = self.get_total_pages(page, number_items)
        if (page == number_of_total_pages) & (remain != 0):
            limit = offset + remain
        else:
            limit = offset + maximun_item_per_page
        return limit

