from tornado.web import Application

from . import api

__all__ = ('app',)

app = Application(handlers=api.handlers)
