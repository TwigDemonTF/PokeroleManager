# Test client + database

import pytest
from Api import app, database

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        database.create_all()
        yield app.test_client()
        database.drop_all()
