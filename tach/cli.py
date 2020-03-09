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


@main.command()
@click.option('-o', '--output', default='erd.png', help='Output filename')
def erd(output):
    """Draw an entity relation diagram for the database."""
    from .models import db
    import eralchemy
    eralchemy.main.switch_input_class_to_method[db.Model.__name__] = \
        eralchemy.main.declarative_to_intermediary
    eralchemy.render_er(db.Model(), output)
