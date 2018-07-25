import tornado.ioloop
import tornado.web

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("usercookie")
        self.redirect("/")

    def post(self):
        self.clear_cookie("usercookie")
        self.redirect("/")
