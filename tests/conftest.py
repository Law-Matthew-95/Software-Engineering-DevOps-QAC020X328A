import pytest
from flask import Flask
from website import create_app , db
from website.models import User

@pytest.fixture()
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'adhfJJFhfh823gb3k2j4j5nk2hjb5k2jb'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['DEBUG'] = False
    return app

@pytest.fixture()
def test_client(app):
    with app.test_client() as client:
        yield client
    
@pytest.fixture(autouse=True)
def setup_db(app):
    with app.app_context():
        # Create tables in the in-memory database
        db.session.remove()
        db.drop_all()
        db.create_all()

        # Add a test user with an existing email
        existing_user = User(
            email='test3@gmail.com',
            first_name='existing',
            last_name='user'
        )
        db.session.add(existing_user)
        db.session.commit()

    yield
    
