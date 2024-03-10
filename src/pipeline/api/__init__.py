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
    app.config['SQLALCHEMY_DATABASE_URI_DATALAKE'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_DATABASE_URI_ROOTS'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST_RAICES')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    from src.pipeline.config.db import init_db_dataleak, init_db_raices
    init_db_dataleak(app)
    init_db_raices(app)

    consumers(app)

    LOGGER.info("Pipeline App created")

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app