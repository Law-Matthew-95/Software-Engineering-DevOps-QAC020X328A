import pytest
from flask import Flask , request , jsonify
from website import create_app , db
from website.models import User , Ticket
from website.auth import sign_up, login, logout, users, alltickets, edittickets


def test_client(app):
    """
    A Flask test client. An instance of :class:`flask.testing.TestClient` by default.
    """
    with app.test_client() as client:
        yield client

def test_signup(test_client):
    """
    GIVEN a Flask application
    WHEN the '/sign-up' page is posted to (POST)
    THEN check the response is valid
    """
    data = {
        'email':'test@gmail.com',
        'first_name':'test',
        'last_name':'tester',
        'password1':'1234567890',
        'password2':'1234567890',
    }
    response = test_client.post('/sign-up', data=data , follow_redirects=True)
    
    assert response.status_code == 200

def test_empty_email(test_client):
    data = {
        'email': '',
        'first_name': '',
        'last_name': '',
        'password1': '',
        'password2': '',
    }
    response = test_client.post('/sign-up', data=data, follow_redirects=True)
    assert b'Email must be greater than 3 characters.' in response.data

def test_empty_first_name(test_client):
    data = {
        'email': 'test@gmail.com',
        'first_name': '',
        'last_name': 'tester',
        'password1': 'password123',
        'pawword2': 'password123',
    }
    response = test_client.post('/sign-up', data=data, follow_redirects=True)
    assert b'First name must be greater than 1 character.' in response.data

def test_empty_last_name(test_client):
    data = {
        'email': 'test@gmail.com',
        'first_name': 'test',
        'last_name': '',
        'password1': 'password123',
        'password2': 'password123',
    }
    response = test_client.post('/sign-up', data=data, follow_redirects=True)
    assert b'Last name must be greater than 1 character.' in response.data

def test_password_mismatch(test_client):
    data = {
        'email': 'test2@gmail.com',
        'first_name': 'test',
        'last_name': 'tester',
        'password1': 'password123',
        'password2': 'differentpassword',
    }
    response = test_client.post('/sign-up', data=data, follow_redirects=True)
    assert b"Passwords do not match." in response.data

def test_short_password(test_client):
    data = {
        'email': 'test2@gmail.com',
        'first_name': 'test',
        'last_name': 'tester',
        'password1': '123',
        'password2': '123',
    }
    response = test_client.post('/sign-up', data=data, follow_redirects=True)
    assert b"Password must be at least 7 characters." in response.data
    
def test_existing_email(test_client):
    data = {
        'email': 'test3@gmail.com',
        'first_name': 'test',
        'last_name': 'tester'
    }
    response = test_client.post('/sign-up', data=data, follow_redirects=True)
    assert b'Email already exists.' in response.data

def test_logout(test_client):
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
