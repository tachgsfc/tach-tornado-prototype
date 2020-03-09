from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.tornado import TornadoPlugin

__all__ = ('spec',)

spec = APISpec(
    title=__name__.split('.')[0],
    version='0.1.0',
    openapi_version='3.0.2',
    plugins=[MarshmallowPlugin(), TornadoPlugin()]
)
