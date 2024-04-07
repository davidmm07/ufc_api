from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)
    from app.routes import main_blueprint
    app.register_blueprint(main_blueprint)
    @app.cli.command("seed_db")
    def seed_db_command():
        from seed_data import seed_data
        seed_data()

    return app
