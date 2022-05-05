import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.book import Book

@pytest.fixture
def app():
    app = create_app({"TESTING":True})

    # request_finished decorator create a new database session after
    # a request ad described below.
    # the function expire_session, will be invoked after any request is completed
    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    # lets various functionality in Flask determine what the current running app is.
    # This is particularly important when accessing the database associated with the app.
    with app.app_context():
        db.create_all()   # the start of each test
        yield app         
        #  The lines after this yield statement will run after the test using the app has been completed.
    
    with app.app_context():
        db.drop_all()


@pytest.fixture
# make a test client ti simulate a client making HTTP requests
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_books(app):
    ocean_book = Book(title="Ocean Book",description="watr 4evr")
    mountain_book = Book(title="Mountain Book",description="i luv 2 climb rocks")

    db.session.add_all([ocean_book, mountain_book])
    db.session.commit()