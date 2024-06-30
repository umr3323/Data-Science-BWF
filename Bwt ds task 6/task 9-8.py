class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

# Example usage:
admin = Admin('John', 'Doe', 'jdoe', 'jdoe@example.com', 'NY')
admin.privileges.privileges = ['can add post', 'can delete post', 'can ban user']
admin.describe_user()
admin.privileges.show_privileges()
