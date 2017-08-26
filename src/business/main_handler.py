# -*- coding: utf-8 -*-

import jwt
import tornado.web

import datetime
import time
import json

from component.book import Book
from component.shop import Shop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        self.write("Hello, world")


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # The value of the 'Access-Control-Allow-Origin' header in the response must not be the wildcard '*' when the request's credentials mode is 'include'. Origin 'http://localhost:4200' is therefore not allowed access. The credentials mode of requests initiated by the XMLHttpRequest is controlled by the withCredentials attribute.
        #self.set_header('Access-Control-Allow-Origin', 'http://kylin-ux.com:4200')
        self.set_header('Access-Control-Allow-Origin', 'http://localhost:4200')
        #self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        # set-cookie in response not set for Angular2 post request
        # because CORS
        # return this.http.post('http://localhost:8888/api/query_mshopbook_init_data', JSON.stringify({}), { withCredentials: true })
        # The value of the 'Access-Control-Allow-Credentials' header in the response is 'True' which must be 'true' when the request's credentials mode is 'include'. Origin 'http://localhost:4200' is therefore not allowed access. The credentials mode of requests initiated by the XMLHttpRequest is controlled by the withCredentials attribute.
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

    def get_current_user(self):
        return self.get_secure_cookie("user")

    #def write(self, chunk):
    #    super(BaseHandler, self).write(chunk)


# class LoginHandler(BaseHandler):
#     def get(self):
#         print('hello get')
#         #self.redirect("http://localhost:4200/content")
#         self.write("Hello, world")
#     def post(self):
#         param = self.request.body.decode('utf-8')
#         param = json.loads(param)
#         #self.write({'token': 'kylin_token'})
#         if param['username'] == 'admin' and param['password'] == '111111':
#             self.write({'...': '...'})
#         else:
#             self.write({
#                 "request" : "/api/authenticate",
#                 "error_code" : "20502",
#                 "error" : "Need you follow uid."
#             })

class LoginHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        incorrect = self.get_secure_cookie("incorrect")
        if incorrect and int(incorrect) > 20:
            self.write('<center>blocked</center>')
            return
        self.render('login.html')

    @tornado.gen.coroutine
    def post(self):
        incorrect = self.get_secure_cookie("incorrect")
        if incorrect and int(incorrect) > 200:
            self.write({
                "request" : "/api/authenticate",
                "error_code" : "20502",
                "error" : "Need you follow uid."
            })
            return

        # getusername = tornado.escape.xhtml_escape(self.get_argument("username"))
        # getpassword = tornado.escape.xhtml_escape(self.get_argument("password"))

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        getusername = param['username']
        getpassword = param['password']
        #self.write({'token': 'kylin_token'})
        print(param)

        if "admin" == getusername and "111111" == getpassword:
            self.set_secure_cookie("user", getusername)
            self.set_secure_cookie("incorrect", "0")
            id_token = jwt.encode({'admin': '111111', 'exp':time.time()+3600}, 'secret', algorithm='HS256').decode('utf8')
            self.write({'id_token': id_token})
            #self.redirect(self.reverse_url("main"))
        else:
            incorrect = self.get_secure_cookie("incorrect") or 0
            increased = str(int(incorrect)+1)
            self.set_secure_cookie("incorrect", increased)
            self.write({
                "request" : "/api/authenticate",
                "error_code" : "20502",
                "error" : "Need you follow uid."
            })


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", self.reverse_url("main")))


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.write("Hello, world")

    @tornado.web.authenticated
    def post(self):
        self.write("Hello, world")


class SaveTemplateHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        import mock

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        print(param)
        self.write({'res':True})



class SingleBookHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        print('hello get')
        #self.redirect("http://localhost:4200/content")
        self.write("Hello, world")

    @tornado.web.authenticated
    def post(self):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        #self.write({'token': 'kylin_token'})
        if param['username'] == 'admin' and param['password'] == '111111':
            self.write({'...': '...'})
        else:
            self.write({
                "request" : "/api/authenticate",
                "error_code" : "20502",
                "error" : "Need you follow uid."
            })


class BookMultiShopHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        user = self.get_current_user()
        print(user)
        param = self.request.body.decode('utf-8')
        param = json.loads(param)

        # out
        # [{'id': '', 'text': ''}, ]
        r = Book.get_book_name_list()
        print(r)
        self.write({'data':r})


class BookMultiShopQueryHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        user = self.get_current_user()
        print(user)
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        print(param)

        book = param['book']

        end = datetime.datetime.now()
        start = end.date() - datetime.timedelta(int(param['period'])-1)

        # out
        # [{'id': '', 'text': ''}, ]
        # [('shop', 'datatype', 'value'), ]
        shop_list = []
        datatype_list = []
        r = Book.query_data_anyshop_anytype(book['id'], start, end)
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
        self.write({'data':data})
        # self.write({'data':[{
        #     'shop': '人邮',
        #     'price': '11.2',
        #     'discount': 5,
        #     'sale': 839,
        #     'comment': 99999,
        #         'inv': 208.178
        #           }]})


class MultiShopBookHandler(BaseHandler):
    """Query last record,
    all datatype
    all template of current user
    all shop list
    all book list
    """

    @classmethod
    def query_data(cls, shop, book, datatype, start, end):
        data = {}
        shop_name = Shop.query_name(shop)
        book_name = Book.query_name(book)
        _data = Book.query_data(shop, book, datatype, start, end)
        if _data is None:
            return data

        data = {
            'shop': {'id': shop, 'text': shop_name},
            'book': {'id': book, 'text': book_name},
            'date': [str(i[0]) for i in _data],
            'value': [i[1] for i in _data]
        }

        return data

    @classmethod
    def query_data_list(cls, shopbook_list, datatype, start, end):
        data = {}
        data['type'] = datatype
        data['data'] = []
        for shopbook in shopbook_list:
            _data = cls.query_data(shopbook[0], shopbook[1], datatype, start, end)
            data['data'].append(_data)
        return data

    @tornado.web.authenticated
    def get(self):
        print('hello get')
        #self.redirect("http://localhost:4200/content")
        self.write("Hello, world")

    @tornado.web.authenticated
    def post(self):
        import mock

        user = self.get_current_user()
        print(user)
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        #self.write({'token': 'kylin_token'})
        # {datatype:xxx, list:[{'shop', 'book'}, {'shop', 'book'}, ...]}, 若参数为空, 则根据用户最后使用的模板查询
        # query by shop+book+datatype
        print('request')
        # type, [(shop, book),] -> [(date, value),]
        from data_model.table import T_Config_Datatype
        from data_model.table import T_Business_Template
        # r = Book.query_data('winshare', '9787115394392', '销量', datetime.date(2017, 7, 27), datetime.datetime.now());


        shop = 'rmydcbs'
        book = '9787115394392'
        datatype = 'price'
        start = datetime.date(2017, 7, 27)
        end = datetime.datetime.now()

        data = self.query_data_list([(shop, book)], datatype, start, end)
        # shopbook_list
        shopbook_list = []
        shop_name_list = Shop.get_shop_name_list()
        book_name_list =  []
        for s in shop_name_list:
            r = Shop.get_book_name_list(s[0])
            shopbook_list.append({'id': s[0], 'text': s[1], 'data':[ {'id': i[0], 'text': i[1]} for i in r]})

        # datatype_list
        r = T_Config_Datatype.query_datatype()
        datatype_list = [{'id': i[0], 'text': i[1]} for i in r]

        # template_list
        r = T_Business_Template.all()
        temp_list = []
        for i in r:
            for t in temp_list:
                if i[0] == t['id']:
                    t['data'].append({'shop': {'id': i[2], 'text':i[3]}, 'book': {'id': i[4], 'text':i[5]}})
                    break
            else:
                temp_list.append({'id': i[0], 'text': i[1], 'data': [{'shop': {'id': i[2], 'text': i[3]}, 'book': {'id': i[4], 'text': i[5]}}]})

        # shopbook_data
        mock.init['shop_book_list'] = shopbook_list
        mock.init['template_list'] = temp_list
        mock.init['datatype_list'] = datatype_list
        mock.init['data'] = data
        self.write(mock.init)


class MultiShopBookQueryHandler(BaseHandler):

    @tornado.web.authenticated
    def post(self):
        import mock

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        # {'data': [{'book': {'text': 'Python参考手册(第4版·修订版)', 'id': '9787115394392'}, 'shop': {'text': '人民邮电出版社官方旗舰店', 'id': 'rmydcbs'}}], 'type': 'price'}
        #self.write({'token': 'kylin_token'})
        # {datatype:xxx, list:[{'shop', 'book'}, {'shop', 'book'}, ...]}, 若参数为空, 则根据用户最后使用的模板查询
        # query by shop+book+datatype
        print(param)
        #_type = param['type']

        # 根据 type shop book, 查询 date, val
        shopbook_list = [(i['shop']['id'], i['book']['id']) for i in param['data']]
        datatype = param['type']
        end = datetime.datetime.now()
        start = end.date() - datetime.timedelta(int(param['period'])-1)

        res = MultiShopBookHandler.query_data_list(shopbook_list, datatype, start, end)
        self.write(res)

class MultiShopBookSaveTemplateHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        import mock

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        print(param)
        # {'text': '123', 'data': [{'book': {'text': 'Python参考手册(第4版·修订版)', 'id': '9787115394392'}, 'shop': {'text': '人民邮电出版社官方旗舰店', 'id': 'rmydcbs'}}], 'id': '123'}
        #self.write({'token': 'kylin_token'})
        # {datatype:xxx, list:[{'shop', 'book'}, {'shop', 'book'}, ...]}, 若参数为空, 则根据用户最后使用的模板查询
        # query by shop+book+datatype
        value = []
        for i in param['data']:
            value.append((i['shop']['id'], i['book']['id']))
        from data_model.table import T_Business_Template
        _id = T_Business_Template.add(param['text'], value)
        self.write({'id':_id})

class ConcernedDataHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        print('hello get')
        #self.redirect("http://localhost:4200/content")
        self.write("Hello, world")

    @tornado.web.authenticated
    def post(self):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        #self.write({'token': 'kylin_token'})
        if param['username'] == 'admin' and param['password'] == '111111':
            self.write({'...': '...'})
        else:
            self.write({
                "request" : "/api/authenticate",
                "error_code" : "20502",
                "error" : "Need you follow uid."
            })
