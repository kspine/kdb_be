

class Indicator:
    @staticmethod
    def query():
        r = T_Basic_Book.query_category_list()
        return [i[0] for i in r]
