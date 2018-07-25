import tornado.ioloop
import tornado.web

from handlers import main_handler, admin_handler, login_handler, logout_handler

settings = {
    "cookie_secret": "a5b35455180f98da1d31808803b49441",
    "login_url": "/login",
    "debug": "true",
}

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", main_handler.MainHandler),
        (r"/admin", admin_handler.AdminHandler),
        (r"/login", login_handler.LoginHandler),
        (r"/logout", logout_handler.LogoutHandler),
    ], **settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()