class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        
        self.privileges = Privileges()


class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


vladi = Admin('Vladi', 'Tetevenski', 'vtet03', 'vtet@example.com', 'Bulgaria')
vladi.describe_user()

vladi.privileges.show_privileges()

print("\nAdding privileges...")
vladi_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
vladi.privileges.privileges = vladi_privileges
vladi.privileges.show_privileges()
