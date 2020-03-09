import click

__all__ = ('main',)


@click.group()
def main():
    pass


@main.command()
@click.option('-h', '--host', default='127.0.0.1', help='Bind to this address')
@click.option('-p', '--port', default=8000, type=int, help='Bind to this port')
def run(host, port):
    """Run the web application."""
    import tornado.ioloop
    from . import web

    web.app.listen(port, host)
    tornado.ioloop.IOLoop.current().start()
