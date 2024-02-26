import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session



def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    from src.auditoria.config.db import init_db
    # Inicializa la DB
    init_db(app)

    from src.auditoria.config.db import db

    import src.auditoria.modules.enrequicimiento.infrastructure.dto

    with app.app_context():
        db.create_all()

    from . import enrequicimiento

    app.register_blueprint(enrequicimiento.bp)

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app