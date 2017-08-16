from common.extern import g_data
from common.extern import g_data_merge
from data_model.db import DbHandler
from data_model.table import T_Basic_ShopBook
from data_model.table import T_Business_Template

from data_model.table import create_table

# init before server listen
def init():
    db_hdl = DbHandler()
    create_table()
    return

    T_Basic_ShopBook.add('rmydcbs', '9787115394392', 'https://detail.tmall.com/item.htm?spm=a1z10.3-b.w4011-9986777119.15.79c15d8JGRW05&id=539853070197&rn=934e2d1ecc4ab188c0bb95e26877b606&abbucket=4')
    exit(0)

    from component.shop import Shop
    Shop.get_shop_list()
    exit(0)

    from component.book import Book
    #_id = T_Business_Template.add('xxx', [('s1', 'b1'),('s2', 'b2')])
    #exit(0)
    _id = T_Business_Template.query(1)
    print(_id)
    exit(0)
    Book.get_book()
    #r = T_Basic_ShopBook.query_shopbook_id('winshare', '9787115394392')
    #print(r)
    import datetime
    # Book.add_data('winshare', '9787115394392', '销量', datetime.datetime.now(), 8);
    r = Book.query_data('winshare', '9787115394392', '销量', datetime.date(2017, 7, 27), datetime.datetime.now());
    print(r)
    exit(0)
