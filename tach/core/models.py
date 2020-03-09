"""Core SQLAlchemy utils."""
from inflection import underscore
from sqlalchemy.ext.declarative import declared_attr

__all__ = ('AutoTableName',)


class AutoTableName:

    @declared_attr
    def __tablename__(cls):
        """Add default table name."""
        return underscore(cls.__name__)
