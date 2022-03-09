from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from app.data_source import DataSource

class HelloRoute(RequestHandler):
    def get(self):
        self.write({'message': 'hello world'})

class StatusRoute(RequestHandler):
    dataSource = None
    def initialize(self):
        self.dataSource = DataSource()
    
    def get(self):
        status = self.dataSource.getStatus()
        json = status.toJSON()
        self.write(json)

class ConfigurationRoute(RequestHandler):
    dataSource = None
    def initialize(self):
        self.dataSource = DataSource()

    def get(self):
        configuration = self.dataSource.getConfiguration()
        json = configuration.toJSON()
        self.write(json)

class FlagStatusRoute(RequestHandler):
    dataSource = None
    def initialize(self):
        self.dataSource = DataSource()

    def get(self):
        status = self.dataSource.getFlagStatus()
        json = status.toJSON()
        self.write(json)

def make_app():
    urls = [
        ("/", HelloRoute),
        ("/status/", StatusRoute),
        ("/configuration/", ConfigurationRoute),
        ("/flag-status/", FlagStatusRoute)
    ]
    return Application(urls)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(5000)
    IOLoop.instance().start()