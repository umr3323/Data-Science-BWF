# admin_test.py

from admin import Admin

admin_user = Admin("John", "Doe", "johndoe", "johndoe@example.com")
admin_user.describe_user()
admin_user.privileges.show_privileges()
