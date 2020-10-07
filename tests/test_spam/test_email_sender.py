from spam.sending_email import Sending, InvalidEmail
import pytest


def test_email_sending():
    """"
    We are going to create a simple test
    The email sending is going to be a class
    to create this class we can selecting Sending() and pressing ALT+ENTER
    then we need to move the Class Sending to spam directory
    to create method we can selecting it and pressing ALT+ENTER
    """
    sending = Sending()
    assert sending is not None


# parametrize the first element is the  receiver then a  list of receivers
@pytest.mark.parametrize(
    'receiver',
    ['jorge.plautz@gmail.com', 'jorgeluiz.plautz@carritech.com']
)
def test_sender(receiver):
    sending = Sending()
    result = sending.send(
        receiver,
        'contato@luchtransportes.com',
        'Curso Python',
        'Turma de primeira',
    )
    assert receiver in result


# test to check if email account is correct
@pytest.mark.parametrize(
    'receiver',
    ['', 'jorgeluiz']
)
def test_invalid_sender(receiver):
    sending = Sending()
    # here we have a context manager and the code inside of this context
    # is going to generate a exception
    with pytest.raises(InvalidEmail):
        sending.send(
            receiver,
            'contato@luchtransportes.com',
            'Curso Python',
            'Turma de primeira',
        )
