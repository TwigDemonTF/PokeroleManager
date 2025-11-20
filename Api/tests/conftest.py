# Test client + database

import pytest
from Api import app, database

import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, root_dir)

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        database.create_all()
        yield app.test_client()
        database.drop_all()
