import datetime

import sqlalchemy
from sqlalchemy import func
from sqlalchemy import desc
from sqlalchemy import distinct

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DATETIME

from data_model.db import DbHandler

Base = declarative_base()

class T_Base():
    db_hdl = DbHandler()
    def __init__():
        self.db_hdl = DbHandler()

class T_User(Base, T_Base):
    # 表的名字:
    __tablename__ = 'T_USER'

    # 表的结构:
    user = Column(String(20), primary_key=True)
    name = Column(String(20))
    password = Column(String(16))

    @classmethod
    def verify(cls, user, password):
        r = cls.db_hdl.session.query("1").filter(cls.user==user, cls.password==password).first()
        if not r:
            return False
        return True

class T_Config_Datatype(Base, T_Base):
    __tablename__ = 'T_CONFIG_DATATYPE'

    # id = Column(Integer, primary_key=True)
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    @classmethod
    def query_datatype(cls):
        r = cls.db_hdl.session.query(cls.id, cls.name).all()
        return r

class T_Config_Category(Base, T_Base):
    __tablename__ = 'T_CONFIG_CATEGORY'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))


class T_Basic_Book(Base, T_Base):
    __tablename__ = 'T_BASIC_BOOK'

    id = Column(Integer, primary_key=True)
    book = Column(String(20))
    name = Column(String(32))
    category = Column(String(32))

    #@staticmethod
    @classmethod
    def query_book_list(cls):
        r = cls.db_hdl.session.query(cls.id).filter().all()
        return r

    @classmethod
    def query_name(cls, book):
        r = cls.db_hdl.session.query(cls.name).filter(cls.book == book).first()
        if r is None:
            return r
        return r[0]

    @classmethod
    def query_book_name_list(cls):
        #book_tuple = tuple([book[0] for book in book_list])
        r = cls.db_hdl.session.query(cls.book, cls.name).filter().all()
        return r

    @classmethod
    def query_book_name_list_by_book(cls, book_list):
        #book_tuple = tuple([book[0] for book in book_list])
        book_tuple = tuple(book_list)
        r = cls.db_hdl.session.query(cls.book, cls.name).filter(cls.book.in_(book_tuple)).all()
        return r

    @classmethod
    def query_book_name_list_by_category(cls, category):
        #book_tuple = tuple([book[0] for book in book_list])
        r = cls.db_hdl.session.query(cls.book, cls.name).filter(cls.category==category).all()
        return r

    @classmethod
    def query_category_list(cls):
        #book_tuple = tuple([book[0] for book in book_list])
        r = cls.db_hdl.session.query(distinct(cls.category)).filter().all()
        return r


class T_Basic_Shop(Base, T_Base):
    __tablename__ = 'T_BASIC_SHOP'

    id = Column(Integer, primary_key=True)
    shop = Column(String(20))
    name = Column(String(32))
    url = Column(String(1024))

    @classmethod
    def query_shop_list(cls):
        # r = cls.db_hdl.session.query(cls.id).filter('shop'==shop, 'book'==book).first()
        r = cls.db_hdl.session.query(cls.shop).filter().all()
        return r

    @classmethod
    def query_name(cls, shop):
        r = cls.db_hdl.session.query(cls.name).filter(cls.shop == shop).first()
        if r is None:
            return r
        return r[0]

    @classmethod
    def query_shop_name_list(cls):
        # r = cls.db_hdl.session.query(cls.id).filter('shop'==shop, 'book'==book).first()
        r = cls.db_hdl.session.query(cls.shop, cls.name).filter().all()
        return r


class T_Basic_ShopBook(Base, T_Base):
    __tablename__ = 'T_BASIC_SHOPBOOK'

    id = Column(Integer, primary_key=True)
    book = Column(String(20))
    shop = Column(String(20))
    url = Column(String(1024))

    @classmethod
    def add(cls, shop, book, url):
        r = cls.db_hdl.session.query(cls.id).filter(cls.shop==shop, cls.book==book).first()
        if r is not None:
            print('existed...')
            return

        cls.db_hdl.session.add(cls(shop=shop, book=book, url=url))
        cls.db_hdl.session.commit()

    @classmethod
    def query_shopbook_id(cls, shop, book):
        # r = cls.db_hdl.session.query(cls.id).filter('shop'==shop, 'book'==book).first()
        r = cls.db_hdl.session.query(cls.id).filter(cls.shop==shop, cls.book==book).first()
        return r

    @classmethod
    def query_book_list(cls, shop):
        # r = cls.db_hdl.session.query(cls.id).filter('shop'==shop, 'book'==book).first()
        r = cls.db_hdl.session.query(cls.book).filter(cls.shop==shop).all()
        return [i[0] for i in r]

    @classmethod
    def query_shop_list(cls, book):
        r = cls.db_hdl.session.query(cls.shop).filter(cls.book==book).all()
        return [i[0] for i in r]

    @classmethod
    def query_shopbook_list(cls):
        r = cls.db_hdl.session.query(cls.shop, cls.book).filter().all()
        return r


class T_Data(Base, T_Base):
    __tablename__ = 'T_DATA'

    # sb_id = Column(Integer, primary_key=True)
    shop = Column(String(20), primary_key=True)
    book = Column(String(20), primary_key=True)
    datatype = Column(String(20), primary_key=True)
    value = Column(Integer)
    date = Column(DATETIME, primary_key=True)

    @classmethod
    def add(cls, shop, book, datatype, date, value):
        cls.db_hdl.session.add(cls(shop=shop, book=book, datatype=datatype, date=date, value=value))
        cls.db_hdl.session.commit()

    @classmethod
    def query(cls, shop, book, datatype, start, end):
        r = cls.db_hdl.session.query(cls.date, cls.value).filter(cls.shop==shop, cls.book==book, cls.datatype==datatype, cls.date>=start, cls.date<end).all()
        return r

    @classmethod
    def query_anyshop_anytype(cls, book, start, end):
        # print(book, start, end)
        # q = cls.db_hdl.session.query(cls.shop, cls.datatype, cls.date, cls.value).filter(cls.book==book, cls.date>=start, cls.date<end)
        # r = q.all()
        # print(q)

        # r = cls.db_hdl.session.query(cls.shop, cls.datatype, func.concat(cls.date), cls.value).filter(cls.book==book, cls.date>=start, cls.date<end).all()
        # r = cls.db_hdl.session.query(cls.shop, cls.datatype, func.concat(func.DATE(cls.date)), cls.value).filter(cls.book==book, cls.date>=start, cls.date<end).all()
        # shop
        # r = cls.db_hdl.session.query(cls.shop, cls.datatype, cls.value).filter(cls.book==book, cls.date>=start, cls.date<end).order_by(cls.date).all()
        # shop -> name # join
        r = cls.db_hdl.session.query(T_Basic_Shop.name, cls.datatype, cls.value).filter(cls.shop == T_Basic_Shop.shop, cls.book==book, cls.date>=start, cls.date<end).order_by(cls.date).all()
        return r


class T_Business_Template(Base, T_Base):
    __tablename__ = 'T_BUSINESS_TEMPLATE'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    date = Column(DATETIME)

    @classmethod
    def add(cls, name, values):
        t = cls(name=name)
        cls.db_hdl.session.add(t)
        cls.db_hdl.session.flush() # or, t.id is None

        _id = t.id

        # select last_insert_id
        _list = []
        for v in values:
            shop = v[0]
            book = v[1]
            _list.append(T_Business_TemplateData(temp_id=t.id, shop=shop, book=book))
        cls.db_hdl.session.bulk_save_objects(_list)
        cls.db_hdl.session.commit()
        return _id

    @classmethod
    def query(cls, temp_id):
        r = cls.db_hdl.session.query(cls.name).filter(cls.id==temp_id).first()
        r = cls.db_hdl.session.query(T_Business_TemplateData.shop, T_Business_TemplateData.book).filter(T_Business_TemplateData.temp_id==temp_id).all()
        return r

    @classmethod
    def all(cls):
        #r = cls.db_hdl.session.query(cls.name).filter().first()
        #name = r[0]
        r = cls.db_hdl.session.query(cls.id, cls.name, T_Business_TemplateData.shop, T_Basic_Shop.name, T_Business_TemplateData.book, T_Basic_Book.name).filter(cls.id == T_Business_TemplateData.temp_id, T_Business_TemplateData.shop == T_Basic_Shop.shop, T_Business_TemplateData.book == T_Basic_Book.book).all()
        return r


class T_Business_TemplateData(Base, T_Base):
    __tablename__ = 'T_BUSINESS_TEMPLATE_DATA'

    temp_id = Column(Integer, primary_key=True)
    shop = Column(String(20), primary_key=True)
    book = Column(String(20), primary_key=True)

class T_Business_Formula(Base, T_Base):
    __tablename__ = 'T_BUSINESS_FORMULA'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    formula = Column(String(64))

    @classmethod
    def query_all(cls):
        r = cls.db_hdl.session.query(cls.id, cls.name, cls.formula).filter().all()
        return r

    def query(cls, id):
        r = cls.db_hdl.session.query(cls.name, cls.formula).filter(cls.id == id).first()
        return r

class T_Business_Monitor_Data(Base, T_Base):
    __tablename__ = 'T_BUSINESS_MONITOR_DATA'

    id = Column(Integer, primary_key=True)
    shop = Column(String(20))
    book = Column(String(20))
    datatype = Column(String(20))
    value = Column(String(20))
    value_old = Column(String(20))
    formula_id = Column(String(64)) #id
    date = Column(DATETIME)

    @classmethod
    def add(cls, shop, book, datatype, value, value_old, formula_id):
        cls.db_hdl.session.add(cls(shop=shop, book=book, datatype=datatype, value=value, value_old=value_old, formula_id=formula_id, date=datetime.datetime.now()))
        cls.db_hdl.session.commit()

    @classmethod
    def query_all(cls):
        r = cls.db_hdl.session.query(cls.shop, cls.book, cls.value, cls.formula, cls.date).filter().all()
        return r

    @classmethod
    def query_by_book_formula(cls, book, formula_id):
        #r = cls.db_hdl.session.query(cls.shop, cls.book, cls.datatype, cls.value, cls.formula_id, cls.date).filter(cls.book == book, cls.formula_id==formula_id).all()
        r = cls.db_hdl.session.query(T_Basic_Shop.name, T_Basic_Book.name, T_Config_Datatype.name, cls.value, T_Business_Formula.name, cls.date).filter(cls.book == book, cls.formula_id==formula_id, cls.shop==T_Basic_Shop.shop, cls.book==T_Basic_Book.book, T_Config_Datatype.id==cls.datatype, T_Business_Formula.id==cls.formula_id).all()
        return r

class T_OpHistory(Base, T_Base):
    __tablename__ = 'T_OP_HISTORY'

    id = Column(Integer, primary_key=True)
    user = Column(String(20))
    business_id = Column(String(20))
    request = Column(String(1024))
    time = Column(DATETIME)

    @classmethod
    def add_request(cls, user, business_id, request):
        cls.db_hdl.session.add(cls(user=user, business_id=business_id, request=request, time=datetime.datetime.now()))
        cls.db_hdl.session.commit()

    @classmethod
    def last_request(cls, user, business_id):
        r = cls.db_hdl.session.query(cls.request).filter(cls.user == user, cls.business_id == business_id).order_by(desc(cls.time)).first()
        if r:
            return r[0]


def create_table():
    db_hdl = DbHandler()
    try:
        T_Basic_Book.metadata.create_all(db_hdl.engine)
    except sqlalchemy.exc.ProgrammingError as e:
        pass

    try:
        T_Basic_Shop.metadata.create_all(db_hdl.engine)
    except sqlalchemy.exc.ProgrammingError as e:
        pass

    try:
        T_Basic_ShopBook.metadata.create_all(db_hdl.engine)
    except sqlalchemy.exc.ProgrammingError as e:
        pass

    try:
        T_Data.metadata.create_all(db_hdl.engine)
    except sqlalchemy.exc.ProgrammingError as e:
        pass

    try:
        T_Business_Template.metadata.create_all(db_hdl.engine)
    except sqlalchemy.exc.ProgrammingError as e:
        pass

    try:
        T_Business_TemplateData.metadata.create_all(db_hdl.engine)
    except sqlalchemy.exc.ProgrammingError as e:
        pass

    try:
        T_Data.metadata.create_all(db_hdl.engine)
    except sqlalchemy.exc.ProgrammingError as e:
        pass
