import catapp
from catapp import app
from catapp import ViewIndex
from catapp import ViewArchive
from catapp import ViewUpdateImage
from catapp import HandleUserRequest
from catapp import Pagination
from catapp import Task
from catapp import Factory
from catapp import CatApi


if __name__ == "__main__":

    maximun_item_per_page = 6
    pagination = Pagination(maximun_item_per_page)
    app.add_url_rule('/', view_func=ViewIndex.as_view('index',
                                                      controller=HandleUserRequest()))
    app.add_url_rule('/update_cat_image',
                     view_func=ViewUpdateImage.as_view('update_cat_image',
                                                       controller=HandleUserRequest()))
    app.add_url_rule('/archive/<int:page>',
                     view_func=ViewArchive.as_view('archive',
                                                   controller=HandleUserRequest(),
                                                   maximun_item_per_page=maximun_item_per_page,
                                                   pagination=pagination))
    app.run(debug=True)
