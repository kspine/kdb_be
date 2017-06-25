import jwt
import tornado.ioloop
import tornado.web
import tornado.options
import os.path
import time
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

import json

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


class MultiShopBookHandler(BaseHandler):
    """Query last record,
    all datatype
    all template of current user
    all shop list
    all book list
    """

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
        self.write(mock.init)


class MultiShopBookQueryHandler(BaseHandler):

    @tornado.web.authenticated
    def post(self):
        import mock

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        #self.write({'token': 'kylin_token'})
        # {datatype:xxx, list:[{'shop', 'book'}, {'shop', 'book'}, ...]}, 若参数为空, 则根据用户最后使用的模板查询
        # query by shop+book+datatype
        print('request')
        print(param['data'])
        #_type = param['type']
        _shop_book = [{'shop':i['shop'], 'book':i['book']} for i in param['data']]

        # 根据 type shop book, 查询 date, val
        res = {}
        res['data'] = []
        for i in range(len(_shop_book)):
            print(i)
            res['data'].append(mock.data_query['data'][0])
        print('+++')
        print(res)
        self.write(res)

class MultiShopBookSaveTemplateHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        import mock

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        print(param)
        #self.write({'token': 'kylin_token'})
        # {datatype:xxx, list:[{'shop', 'book'}, {'shop', 'book'}, ...]}, 若参数为空, 则根据用户最后使用的模板查询
        # query by shop+book+datatype
        print('request')
        self.write({'id':12345})

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


class Application(tornado.web.Application):
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        settings = {
            "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            "login_url": "/login",
            'template_path': os.path.join(base_dir, "template"),
            'static_path': os.path.join(base_dir, "static"),
            'debug':True,
            #"xsrf_cookies": True,
        }

        tornado.web.Application.__init__(self, [
        (r"/", MainHandler),
        (r"/api/authenticate", LoginHandler),
        (r"/api/save_template", MultiShopBookSaveTemplateHandler),
        (r"/api/query_book_mdata", SingleBookHandler),
        (r"/api/query_mshopbook_init_data", MultiShopBookHandler),
        (r"/api/query_mshopbook_data", MultiShopBookQueryHandler),
        (r"/api/query_concerned_data", ConcernedDataHandler),
    ], **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.current().start()
