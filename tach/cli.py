from cleo import Application, Command

__all__ = ('app',)


class RunCommand(Command):
    """Run the web application.

    run
        {--p|port=8000 : Bind to this port}
    """

    def handle(self):
        port = int(self.option('port'))

        import tornado.ioloop
        from . import web

        web.app.listen(port)
        tornado.ioloop.IOLoop.current().start()


app = Application(__name__.split('.')[0])
app.add(RunCommand())
