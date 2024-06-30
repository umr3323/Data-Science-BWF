class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User {self.username} details:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"Hello {self.username}!")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Example usage:
admin = Admin('John', 'Doe', 'jdoe', 'jdoe@example.com', 'NY')
admin.privileges = ['can add post', 'can delete post', 'can ban user']
admin.describe_user()
admin.show_privileges()
