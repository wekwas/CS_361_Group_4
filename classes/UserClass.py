from SchedulingAPP.models import User, Role


class UserClass:
    def __init__(self):
        self.user = User(username=" ", password=" ", email=" ", first_name=" ", last_name=" ")

    def get_username(self):
        return self.user.username

    def set_username(self, new_username):
        if new_username is None:
            raise Exception
        elif len(new_username) > 25:
            raise Exception
        else:
            self.user.username = new_username

    def get_password(self):
        return self.user.username

    def set_password(self, new_password):
        if new_password is None:
            raise Exception
        elif len(new_password) > 25:
            raise Exception
        else:
            self.user.password = new_password

    def get_role(self):
        return self.user.role

    def set_role(self, new_role):
        if new_role is None:
            raise Exception
        elif new_role != Role.supervisor and new_role != Role.instructor and new_role != Role.ta:
            raise Exception
        else:
            self.user.role = new_role

    def get_email(self):
        return self.user.email

    def set_email(self, new_email):
        if new_email is None:
            raise Exception
        elif len(new_email) > 40:
            raise Exception
        else:
            self.user.email = new_email

    def get_first_name(self):
        return self.user.first_name

    def set_first_name(self, new_first_name):
        if new_first_name is None:
            raise Exception
        elif len(new_first_name) > 25:
            raise Exception
        else:
            self.user.first_name = new_first_name

    def get_last_name(self):
        return self.user.last_name

    def set_last_name(self, new_last_name):
        if new_last_name is None:
            raise Exception
        elif len(new_last_name) > 25:
            raise Exception
        else:
            self.user.last_name = new_last_name

    def add_user(self):
        try:
            User.objects.get(username=self.user.username)
        except:
            self.user.save()
            return
        raise Exception

    def delete_user(self):
        self.user.delete()



