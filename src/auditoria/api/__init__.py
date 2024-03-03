import os
import logging
from logging.config import dictConfig
from flask import Flask, render_template, request, url_for, redirect, jsonify, session

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
    app.secret_key = 'v63m!jxj)7+cfsw!^9o-g=t-@7r19#+a(jvl)7^os*b!42-%4c'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    from src.auditoria.config.db import init_db
    # Inicializa la DB
    init_db(app)

    from src.auditoria.config.db import db

    import src.auditoria.modules.enrequicimiento.infrastructure.dto
    from src.auditoria.modules.enrequicimiento.infrastructure.dto import Property

    with app.app_context():
        db.create_all()

        if db.session.query(Property).count() == 0:
            new_property = Property(id="5f2e89f1-27ef-4b3a-80ea-8f68c609fa3a", size_sqft=1000.0, construction_type='Brick', floors=2)

            db.session.add(new_property)
            db.session.commit()
            db.session.close()

    from . import enrequicimiento

    app.register_blueprint(enrequicimiento.bp)

    LOGGER.info("Audit App created")

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app