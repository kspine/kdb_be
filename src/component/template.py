from data_model.table import T_Business_Template

class Template:
    def __init__(self, _id, _name, _value):
        self.id = _id
        self.name = _name
        self.value = _value

    def save(self):
        pass

    def info(self):
        pass

    @staticmethod
    def all():
        book_list = T_BUSINESS_TEMPLATE.query_book_list(shop)
        book_name_list = T_Basic_Book.query_book_name_list(book_list)
        return book_name_list

