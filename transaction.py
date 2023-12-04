class Transaction:
    def __init__(self, user, computer):
        self.user = user
        self.computer = computer

    def get_user(self):
        return self.user

    def get_computer(self):
        return self.computer
