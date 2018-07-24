import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item1", "Item2", "Item3"]
        self.render("../html/main.html", items=items)