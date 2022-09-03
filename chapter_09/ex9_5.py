# 9-5. Login Attempts
class User:
    """model a user"""

    def __init__(self, first_name, last_name, **user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        """increment the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset the value of login_attempts to 0"""
        self.login_attempts = 0


user = User('Tao', 'Song')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
