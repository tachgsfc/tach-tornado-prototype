from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin

from .core.api import spec
from . import models


class CircularSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.Circular


class CircularHandler(SessionMixin, RequestHandler):
    def get(self, number):
        """Get a GCN Circular.
        ---
        description: Get a GCN Circular
        responses:
            200:
                description: A GCN Circular
                schema:
                    $ref: '#/definitions/Circular'
        """
        schema = CircularSchema()
        return schema.dumps(self.session.query(models.Circular).query.get(number))


schemas = [CircularSchema]
handlers = [(r'/circular/([0-9]+)', CircularHandler)]

for schema in [CircularSchema]:
    spec.components.schema(schema.Meta.model.__name__, schema=schema)
for handler in handlers:
    spec.path(urlspec=handler)
