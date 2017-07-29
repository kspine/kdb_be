import tornado.ioloop
import tornado.options
from tornado.options import define, options

import first_module
from application.application import Application

from helper import config
from util.log import logger

from init import init

port = config.ConfigHelper.get_server_port()
define("port", default=port, help="run on the given port", type=int)

if __name__ == "__main__":
    init()
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.current().start()
