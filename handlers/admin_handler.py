import tornado.ioloop
import tornado.web

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../html/admin.html")
