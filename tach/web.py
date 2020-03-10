from pkg_resources import resource_filename
from tornado.web import Application, StaticFileHandler

from . import api
from . import models

__all__ = ('app',)

app = Application(
    [*api.handlers,
     (r'/static/(.*)', StaticFileHandler, {'path': resource_filename(__name__, 'static')})],
    db=models.db)
