from spam.sending_email import Sending
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


# parametrize o primeiro elemento será o receiver depois um lista com os receivers
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
