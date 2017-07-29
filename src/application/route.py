#-*- coding: utf-8 -*-

from business.main_handler import MainHandler
from business.main_handler import LoginHandler
from business.main_handler import MultiShopBookSaveTemplateHandler
from business.main_handler import SingleBookHandler
from business.main_handler import MultiShopBookHandler
from business.main_handler import MultiShopBookQueryHandler
from business.main_handler import ConcernedDataHandler

handlers = [
    (r"/", MainHandler),
    (r"/api/authenticate", LoginHandler),
    (r"/api/save_template", MultiShopBookSaveTemplateHandler),
    (r"/api/query_book_mdata", SingleBookHandler),
    (r"/api/query_mshopbook_init_data", MultiShopBookHandler),
    (r"/api/query_mshopbook_data", MultiShopBookQueryHandler),
    (r"/api/query_concerned_data", ConcernedDataHandler)
]
