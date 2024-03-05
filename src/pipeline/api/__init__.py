import os
import logging
from logging.config import dictConfig

from flask import Flask

LOGGER = logging.getLogger()


def consumers(app):
    import threading
    import src.pipeline.modules.information.infrastructure.consumers as information

    threading.Thread(target=information.subscribe_to_events, args=(app,)).start()


def create_app():
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    app = Flask(__name__, instance_relative_config=True)

    consumers(app)

    LOGGER.info("Pipeline App created")

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app