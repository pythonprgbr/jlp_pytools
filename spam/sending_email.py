class Sending(object):
    def send(self, receiver, sender, subject, body):
        if '@' not in receiver:
            raise InvalidEmail(f'Email from sender account is not valid: {receiver}')
        return receiver


class InvalidEmail(Exception):
    pass
