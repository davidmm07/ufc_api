import pytest
from app import create_app, db
from config import Config

@pytest.fixture
def app():
    app = create_app(Config)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
