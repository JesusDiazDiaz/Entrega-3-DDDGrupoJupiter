import os
import logging
from logging.config import dictConfig

from flask import Flask

LOGGER = logging.getLogger()


def consumers(app):
    import threading
    import src.pipeline.modules.validation.infrastructure.consumer as properties

    threading.Thread(target=properties.subscribe_to_events, args=(app,)).start()


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

    app.config['SQLALCHEMY_BINDS'] = {
        'datalake': f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DATALAKE_DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DATALAKE_DB_NAME')}",
        'roots': f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('MAIN_DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('MAIN_DB_NAME')}"
    }

    from src.pipeline.config.db import init_db_datalake, init_db_raices
    init_db_datalake(app)
    init_db_raices(app)

    consumers(app)

    LOGGER.info("Pipeline App created")

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app