import click

__all__ = ('main',)


@click.group()
def main():
    pass


@main.command()
@click.option('-p', '--port', default=8000, type=int, help='Bind to this port')
def run(port):
    """Run the web application."""
    import tornado.ioloop
    from . import web

    web.app.listen(port)
    tornado.ioloop.IOLoop.current().start()
