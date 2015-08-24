import tornado.ioloop
import tornado.web
from tornado import gen

class MainHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
