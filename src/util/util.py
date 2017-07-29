import tornado
from common.extern import g_executor

def background(func):
    def wrapper(*args, **kwargs):
        return g_executor.submit(func, *args, **kwargs)
        # return tornado.ioloop.IOLoop.current().spawn_callback(func, *args, **kwargs)
    return wrapper
