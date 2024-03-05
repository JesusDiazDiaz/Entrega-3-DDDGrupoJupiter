import os
import logging
from logging.config import dictConfig

from flask import Flask

LOGGER = logging.getLogger()


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
    app.secret_key = 'v*1cp%q_v61g%b-&72i90top==@$!#&m&#k+$0+iq5ildlo68b'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    from src.properties.config.db import init_db
    init_db(app)

    from src.properties.config.db import db

    LOGGER.info("Properties App created")

    import src.properties.modules.listings.infrastructure.dto
    from . import main

    with app.app_context():
        db.create_all()

    app.register_blueprint(main.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app