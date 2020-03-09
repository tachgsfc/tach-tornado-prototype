import sqlalchemy as sa
import sqlalchemy_utils as su
from tornado_sqlalchemy import SQLAlchemy

from .core.models import AutoTableName

db = SQLAlchemy('sqlite://')


class Circular(AutoTableName, db.Model):
    number = sa.Column(sa.Integer, nullable=False, primary_key=True)
    sender = sa.Column(su.EmailType, nullable=False)
    received = sa.Column(sa.DateTime, nullable=False)
    subject = sa.Column(sa.UnicodeText, nullable=False)
    body = sa.Column(sa.UnicodeText, nullable=False)
