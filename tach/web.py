from tornado.web import Application

from . import api
from . import models

__all__ = ('app',)

app = Application(handlers=api.handlers, db=models.db)
