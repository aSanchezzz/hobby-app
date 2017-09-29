import tornado.ioloop
import tornado.web
import tornado.log
import os

PORT = int(os.environ.get('PORT', '8888'))

class MainHandler(tornado.web.RequestHandler):
  def get(self):
      self.set_header("Content-Type", 'text/plain')
      self.write("Hello, World")

class YouHandler(tornado.web.RequestHandler):
    def get(self, name):
        self.set_header("Content-Type", 'text-plain')
        self.write("Hello, {}".format(name))

class BlahHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", 'text-plain')
        self.write("Blahblahblahblah")

def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
    (r"/hello/(.*)", YouHandler),
    (r"/blah", BlahHandler),
  ], autoreload=True)

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
