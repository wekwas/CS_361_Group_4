from SchedulingAPP.models import User, Role


def get_username(user):
    return user.username


def set_username(user, new_username):
    if new_username is None:
        raise Exception("New username is null")
    elif len(new_username) > 25:
        raise Exception("New username is > 25")
    else:
        user.username = new_username


def get_password(user):
    return user.password


def set_password(user, new_password):
    if new_password is None:
        raise Exception("New password is null")
    elif len(new_password) > 25:
        raise Exception("New password is > 25")
    else:
        user.password = new_password


def get_role(user):
    return user.role


def set_role(user, new_role):
    if new_role is None:
        raise Exception("New role is null")
    elif new_role != Role.supervisor and new_role != Role.instructor and new_role != Role.ta:
        raise Exception("New role isn't TA, instructor, or supervisor")
    else:
        user.role = new_role


def get_email(user):
    return user.email


def set_email(user, new_email):
    if new_email is None:
        raise Exception("New email is null")
    elif len(new_email) > 40:
        raise Exception("New email is > 40")
    else:
        user.email = new_email


def get_first_name(user):
    return user.first_name


def set_first_name(user, new_first_name):
    if new_first_name is None:
        raise Exception("New first_name is null")
    elif len(new_first_name) > 25:
        raise Exception("New first_name is > 25")
    else:
        user.first_name = new_first_name


def get_last_name(user):
    return user.last_name


def set_last_name(user, new_last_name):
    if new_last_name is None:
        raise Exception("New last_name is null")
    elif len(new_last_name) > 25:
        raise Exception("New last_name is > 25")
    else:
        user.last_name = new_last_name


def get_full_name(user):
    return user.__str__


def exists(username):
    try:
        User.objects.get(username=username)
        return True
    except:
        return False


def add_user(username, password, role, email, first_name, last_name):
    if exists(username):
        raise Exception("Username already exists")
    else:
        new_user = User(username=" ", password=" ", email=" ", first_name=" ", last_name=" ")
        try:
            set_username(new_user, username)
            set_password(new_user, password)
            set_role(new_user, role)
            set_email(new_user, email)
            set_first_name(new_user, first_name)
            set_last_name(new_user, last_name)
            new_user.save()
        except:
            return Exception("Incorrect data")


def delete_user(username):
    if exists(username):
        User.objects.get(username=username).delete()
    else:
        raise Exception("Username doesn't exists")

