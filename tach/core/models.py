"""Core SQLAlchemy utils."""
from inflection import underscore
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base

__all__ = ('Model',)


class AutoTableName:

    @declared_attr
    def __tablename__(cls):
        """Add default table name."""
        return underscore(cls.__name__)


Model = declarative_base(cls=AutoTableName)
