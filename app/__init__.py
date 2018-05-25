import logging

import falcon

from app.config import parser, settings
from app.middleware import CrossDomain, JSONTranslator
from app.resources.root import RootResources, Resource
from app.util.config import setup_vyper
from app.util.error import error_handler
from app.util.logging import setup_logging
from falcon_multipart.middleware import MultipartMiddleware

logger = logging.getLogger(__name__)

_storage_path = './uploaded_files'


def configure(**overrides):
    logging.getLogger("vyper").setLevel(logging.WARNING)
    setup_vyper(parser, overrides)


def create_app():
    setup_logging()

    app = falcon.API(
        middleware=[
            CrossDomain(),
            # JSONTranslator(),
            MultipartMiddleware()
        ],
    )

    app.add_error_handler(Exception, error_handler)

    _setup_routes(app)

    return app


def start():
    logger.info("Environment: {}".format(settings.get("ENV_NAME")))


def _setup_routes(app):
    app.add_route("/", RootResources())
    images = Resource(_storage_path)
    app.add_route('/images', images)
