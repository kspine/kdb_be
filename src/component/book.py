from data_model.table import T_Basic_Book
from data_model.table import T_Basic_ShopBook
from data_model.table import T_Data


class Book:
    def __init__(self, _id):
        self.id = _id

    @staticmethod
    def get_book():
        return T_Basic_Book.query_book_list()

    @staticmethod
    def get_book_name_list():
        r = T_Basic_Book.query_book_name_list()
        return [{'id':i[0], 'text':i[1]} for i in r]
    # 单品页
    def get_book_data(self, _type, _start, _end):
        # id, start, end, type
        pass

    @staticmethod
    def query_name(book):
        r = T_Basic_Book.query_name(book)
        return r

    @staticmethod
    def add_data(shop, book, datatype, date, value):
        # r = T_Basic_ShopBook.query_shopbook_id(shop, book)
        # if r is None:
        #     print('shop+book not existed')
        #     return
        # sb_id = r[0]
        # T_Data.add(sb_id, datatype, date, value)
        T_Data.add(shop, book, datatype, date, value)

    @staticmethod
    def query_data(shop, book, datatype, start, end):
        # r = T_Basic_ShopBook.query_shopbook_id(shop, book)
        # if r is None:
        #     print('shop+book not existed')
        #     return
        # sb_id = r[0]
        # r = T_Data.query(sb_id, datatype, start, end)
        r = T_Data.query(shop, book, datatype, start, end)
        return [(i[0].date(), i[1]) for i in r]

    @staticmethod
    def query_data_anyshop_anytype(book, start, end):
        r = T_Data.query_anyshop_anytype(book, start, end)
        return [(i[0], i[1], i[2]) for i in r]


    @staticmethod
    def add_data_many(value_list):
        # [(shop, book, datatype, date, value)]
        for i in value_list:
            Book.add_data(i[0], i[1], i[2], i[3], i[4])

    @staticmethod
    def query_data_table(book, start, end):
        # out
        # [{'id': '', 'text': ''}, ]
        # [('shop', 'datatype', 'value'), ]
        shop_list = []
        datatype_list = []
        r = Book.query_data_anyshop_anytype(book, start, end)
        for i in r:
            if i[1] not in datatype_list:
                datatype_list.append(i[1])
            if i[0] not in shop_list:
                shop_list.append(i[0])

        c = 0
        res = []
        for shop in shop_list:
            for datatype in datatype_list:
                res_ = []
                first = True
                first_val = 0
                last_val = 0
                for i in r:
                    if i[0] == shop and i[1] == datatype:
                        res_.append(i[2])
                        if first:
                            first_val = i[2]
                            first = False
                        last_val = i[2]
                if datatype == 'sale' or datatype == 'comment':
                    #res.append((shop, datatype, last_val-first_val))
                    res.append((shop, datatype, res_[-1]-res_[0]))
                else:
                    res.append((shop, datatype, round(sum(res_)/len(res_),2)))
        # [{'shop': '', 'price': '1', 'sale': 2}, ]
        data = []
        for i in res:
            for shop in data:
                if i[0] == shop['shop']:
                    shop.setdefault(i[1], i[2])
                    break
            else:
                data.append({'shop': i[0], i[1]: i[2]})

        for i in data:
            for k in ['shop', 'price', 'discount', 'sale', 'comment', 'inv']:
                if k not in i:
                    i[k] = 0
        return data
