
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DATETIME

from data_model.db import DbHandler

Base = declarative_base()

class T_Base():
    db_hdl = DbHandler()
    def __init__():
        self.db_hdl = DbHandler()

class T_User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


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
    def query_book_name_list(cls, book_list):
        #book_tuple = tuple([book[0] for book in book_list])
        book_tuple = tuple(book_list)
        r = cls.db_hdl.session.query(cls.book, cls.name).filter(cls.book.in_(book_tuple)).all()
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
    def query_shopbook_id(cls, shop, book):
        # r = cls.db_hdl.session.query(cls.id).filter('shop'==shop, 'book'==book).first()
        r = cls.db_hdl.session.query(cls.id).filter(cls.shop==shop, cls.book==book).first()
        return r

    @classmethod
    def query_book_list(cls, shop):
        # r = cls.db_hdl.session.query(cls.id).filter('shop'==shop, 'book'==book).first()
        r = cls.db_hdl.session.query(cls.book).filter(cls.shop==shop).all()
        return [i[0] for i in r]

class T_Data(Base, T_Base):
    __tablename__ = 'T_DATA'

    sb_id = Column(Integer, primary_key=True)
    datatype = Column(String(20))
    value = Column(Integer)
    date = Column(DATETIME)

    @classmethod
    def add(cls, sb_id, datatype, date, value):
        cls.db_hdl.session.add(cls(sb_id=sb_id, datatype=datatype, date=date, value=value))
        cls.db_hdl.session.commit()

    @classmethod
    def query(cls, sb_id, datatype, start, end):
        r = cls.db_hdl.session.query(cls.date, cls.value).filter(cls.sb_id==sb_id, cls.date>=start, cls.date<end).all()
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
