import tornado.ioloop
import tornado.web

import json

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        #self.set_header('Access-Control-Allow-Origin', 'http://kylin-ux.com:4200')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

    #def write(self, chunk):
    #    super(BaseHandler, self).write(chunk)


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        self.write("Hello, world")

class LoginHandler(BaseHandler):
    def get(self):
        print('hello get')
        #self.redirect("http://localhost:4200/content")
        self.write("Hello, world")
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

class SingleBookHandler(BaseHandler):
    def get(self):
        print('hello get')
        #self.redirect("http://localhost:4200/content")
        self.write("Hello, world")
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
    def get(self):
        print('hello get')
        #self.redirect("http://localhost:4200/content")
        self.write("Hello, world")
    def post(self):
        import mock

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        #self.write({'token': 'kylin_token'})
        # {datatype:xxx, list:[{'shop', 'book'}, {'shop', 'book'}, ...]}, 若参数为空, 则根据用户最后使用的模板查询
        # query by shop+book+datatype
        print('request')
        self.write(mock.mb)

class ConcernedDataHandler(BaseHandler):
    def get(self):
        print('hello get')
        #self.redirect("http://localhost:4200/content")
        self.write("Hello, world")
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

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/authenticate", LoginHandler),
        (r"/api/query_book_mdata", SingleBookHandler),
        (r"/api/query_mshopbook_data", MultiShopBookHandler),
        (r"/api/query_concerned_data", ConcernedDataHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
