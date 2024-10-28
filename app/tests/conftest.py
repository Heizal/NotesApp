import pytest
# import create_App function from our app.py file
from app.app import create_app
from os import environ
from flask_migrate import upgrade

# Define fixture function with decorator
@pytest.fixture
# run create_app() function to have access to our application
def client():
    environ['DATABASE_URL'] = 'sqlite://'
    app = create_app()
    # within the application context yeild this
    # yield is similar to return but also allows the code to run even after the function is done running.
    with app.app_context():
        upgrade()
        yield app.test_client()