import tornado.ioloop
import tornado.web
import utils.user_checker

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("usercookie"):
            self.render("../html/login.html")
        else:
            self.render("../html/logout.html", login=self.get_secure_cookie("usercookie"))

    def post(self):
        if not utils.user_checker.admin(self.get_argument("login"), self.get_argument("password")):
            self.set_secure_cookie("usercookie", self.get_argument("login"))
            self.redirect("/")
        else:
            self.set_secure_cookie("admincookie", self.get_argument("login"))
            self.redirect("/admin")
