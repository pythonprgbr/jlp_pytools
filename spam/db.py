class Session:
    contador = 0
    users = []
    def save(self, user):
        Session.contador += 1
        user.id = Session.contador
        self.users.append(user)

    def list(self):
        return self.users

    def roll_back(self):
        # just to clean the session cleaning the users from the list
        return self.users.clear()

    def close(self):
        pass


class Connection():
    def create_session(self):
        return Session()

    def close(self):
        pass