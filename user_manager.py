from user import User

class UserManager:
    def __init__(self):
        self.users = []

    def create_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def display_users(self):
        print("Users:")
        for index, user in enumerate(self.users):
            print(f"{index + 1}. {user.get_name()}")
        print()
