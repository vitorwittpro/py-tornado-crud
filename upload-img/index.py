import tornado.web
import tornado.ioloop


class uploadHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files['imgFile']

        for file in files:
            fh = open(f"upload/{file.filename}", "wb")
            fh.write(file.body)
            fh.close()

        self.write(f"http://localhost:8080/img/{file.filename}")

    def get(self):
        self.render("index.html")


if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'}) 
    ])

    app.listen(8080)
    print('Server listening on port 8080')

    tornado.ioloop.IOLoop.instance().start()