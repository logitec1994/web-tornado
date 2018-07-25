import tornado.ioloop
import tornado.web

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_secure_cookie("usercookie") == b"admin":
            self.render("../html/admin.html", text="Admin text for admin page")
        else:
            self.render("../html/admin.html", text="You dont have access for this page")
