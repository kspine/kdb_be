

class Shop:
    def __init__(self, _id):
        self.id = _id

    @staticmethod
    def get_shop_list():
        pass

    def get_book_list(self):
        pass

    @staticmethod
    def query_shopbook_id(shop, book):
        r = T_Basic_ShopBook.query_shopbook_id(shop, book)
        return r
