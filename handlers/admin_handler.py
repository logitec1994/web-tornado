import tornado.ioloop
import tornado.web

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Admin Section")
