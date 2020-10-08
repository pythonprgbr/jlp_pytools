import pytest

from spam.db import Connection
from spam.models import User


@pytest.fixture
def connection():
    # to connect to BD is necessary a connection
    # connection is responsible for the authentication (login and password)
    # here we have a exemplo of generator function -> see objects pythonico
    # Setuo fase
    connection_obj = Connection()
    yield connection_obj
    # Tear-down
    connection_obj.close()


@pytest.fixture
def session(connection):
    # when we have a connection we can start a session
    # throught session we can make the BD operation
    session_obj = connection.create_session()
    yield session_obj
    session_obj.roll_back()
    session_obj.close()


def test_user_save(connection, session):
    # creating the simple Model and via session we can save it
    user = User(name='Plautz')
    session.save(user)

    # It is necessary to assert if the user was created and we need to verify
    # if this user has an attribute and this attribute is one instance type integer
    assert isinstance(user.id, int)


def test_users_list(connection, session):
    # creating the simple Model and via session we can save it
    users = [User(name='Plautz'), User(name='Linda')]
    for user in users:
        session.save(user)

    # It is necessary to assert if the users were saved.
    # the uses list is going to returned a session result by method session.list()
    assert users == session.list()
