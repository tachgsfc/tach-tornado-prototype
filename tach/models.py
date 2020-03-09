import sqlalchemy as sa
import sqlalchemy_utils as su

from .core.models import Model


class Circular(Model):
    number = sa.Column(sa.Integer, nullable=False, primary_key=True)
    sender = sa.Column(su.EmailType, nullable=False)
    received = sa.Column(sa.DateTime, nullable=False)
    subject = sa.Column(sa.UnicodeText, nullable=False)
    body = sa.Column(sa.UnicodeText, nullable=False)
