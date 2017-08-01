from data_model.table import T_Basic_Book
from data_model.table import T_Basic_Shop
from data_model.table import T_Basic_ShopBook

class Shop:
    def __init__(self, _id):
        self.id = _id

    @staticmethod
    def get_shop_list():
        shop_list = T_Basic_Shop.query_shop_list()
        return shop_list

    @staticmethod
    def get_shop_name_list():
        shop_name_list = T_Basic_Shop.query_shop_name_list()
        return shop_name_list

    @staticmethod
    def get_book_list(shop):
        book_list = T_Basic_ShopBook.query_book_list(shop)
        return book_list

    @staticmethod
    def query_name(shop):
        r = T_Basic_Shop.query_name(shop)
        return r

    @staticmethod
    def get_book_name_list(shop):
        book_list = T_Basic_ShopBook.query_book_list(shop)
        book_name_list = T_Basic_Book.query_book_name_list(book_list)
        return book_name_list

    @staticmethod
    def query_shopbook_id(shop, book):
        r = T_Basic_ShopBook.query_shopbook_id(shop, book)
        return r
