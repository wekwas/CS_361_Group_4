from SchedulingAPP.models import User


class UserClass:
    def __init__(self, username, password, role, email, first_name, last_name):
        self.username = username
        self.password = password
        self.role = role
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def get_username(self):
        return self.username

    def set_username(self, new_username):
        self.username = new_username

    def get_password(self):
        return self.username

    def set_password(self, new_username):
        self.username = new_username

    def get_role(self):
        return self.role

    def set_role(self, new_role):
        self.role = new_role

    def get_email(self):
        return self.email

    def set_email(self, new_email):
        self.email = new_email

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name



