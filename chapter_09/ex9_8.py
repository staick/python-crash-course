# 9-8. Privileges
class User:
    """model a user"""

    def __init__(self, first_name, last_name, **user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile

    def describe_user(self):
        print(f"The user name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}.")


class Privilege:
    
    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    
    def __init__(self, first_name, last_name, **user_profile):
        super().__init__(first_name, last_name, **user_profile)
        self.privileges = Privilege()


admin = Admin('Tao', 'Song')
admin.privileges.show_privileges()
