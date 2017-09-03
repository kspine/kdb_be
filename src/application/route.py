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
from business.main_handler import UserListQueryHandler
from business.main_handler import UserDeleteHandler
from business.main_handler import UserAddHandler
from business.main_handler import UserEditHandler
from business.main_handler import UserChangePasswordHandler

handlers = [
    (r"/", MainHandler),
    (r"/api/authenticate", LoginHandler),
    (r"/api/save_template", MultiShopBookSaveTemplateHandler),
    (r"/api/query_mshopbook_init_data", MultiShopBookHandler),
    (r"/api/query_mshopbook_data", MultiShopBookQueryHandler),
    (r"/api/query_concerned_init_data", ConcernedDataHandler),
    (r"/api/query_concerned_data", ConcernedDataQueryHandler),
    (r"/api/query_book_mshop_init_data", BookMultiShopHandler),
    (r"/api/query_book_mshop_data", BookMultiShopQueryHandler),
    (r"/api/query_user_list", UserListQueryHandler),
    (r"/api/delete_user", UserDeleteHandler),
    (r"/api/add_user", UserAddHandler),
    (r"/api/edit_user", UserEditHandler),
    (r"/api/change_password", UserChangePasswordHandler),
]
