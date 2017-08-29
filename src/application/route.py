#-*- coding: utf-8 -*-

from business.main_handler import MainHandler
from business.main_handler import LoginHandler
from business.main_handler import MultiShopBookSaveTemplateHandler
from business.main_handler import SingleBookHandler
from business.main_handler import MultiShopBookHandler
from business.main_handler import MultiShopBookQueryHandler
from business.main_handler import ConcernedDataHandler
from business.main_handler import ConcernedDataQueryHandler
from business.main_handler import BookMultiShopHandler
from business.main_handler import BookMultiShopQueryHandler

handlers = [
    (r"/", MainHandler),
    (r"/api/authenticate", LoginHandler),
    (r"/api/save_template", MultiShopBookSaveTemplateHandler),
    (r"/api/query_mshopbook_init_data", MultiShopBookHandler),
    (r"/api/query_mshopbook_data", MultiShopBookQueryHandler),
    (r"/api/query_concerned_init_data", ConcernedDataHandler),
    (r"/api/query_concerned_data", ConcernedDataQueryHandler),
    (r"/api/query_book_mshop_init_data", BookMultiShopHandler),
    (r"/api/query_book_mshop_data", BookMultiShopQueryHandler)
]
