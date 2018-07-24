import tornado.ioloop
import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("usercookie"):
            self.render("../html/login.html")
        else:
            self.render("../html/logout.html", login="Logitec")

    def post(self):
        if not self.get_secure_cookie("usercookie"):
            login = self.get_argument("login")
            password = self.get_argument("password")
            self.set_secure_cookie("usercookie", "username")
            self.redirect("/")
        else:
            self.clear_cookie("usercookie")
            self.redirect("/login")