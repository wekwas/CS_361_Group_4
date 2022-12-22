from SchedulingAPP.models import User, Role


def get_all_users():
    return User.objects.all()

def get_all_tas():
    return User.objects.filter(role="TA")

def get_all_tas():
    User.objects.filter(role='TA').values()


def get_all_instructors():
    User.objects.filter(role='Instructor').values()


def get_all_supervisors():
    User.objects.filter(role='Supervisor').values()


def get_user(username):
    return User.objects.get(username=username)


def get_username(user):
    return user.username


def set_username(user, new_username):
    if new_username is None:
        raise Exception("Username is null")
    elif len(new_username) > 25:
        raise Exception("Username is > 25")
    elif exists(new_username):
        raise Exception("Username already exists")
    else:
        user.username = new_username


def get_password(user):
    return user.password


def set_password(user, new_password):
    if new_password is None:
        raise Exception("Password is null")
    elif len(new_password) > 25:
        raise Exception("Password is too long")
    else:
        user.password = new_password


def get_role(user):
    return user.role


def set_role(user, new_role):
    if new_role is None:
        raise Exception("Role is null")
    elif new_role != Role.supervisor and new_role != Role.instructor and new_role != Role.ta:
        raise Exception("Role not valid")
    else:
        user.role = new_role


def get_email(user):
    return user.email


def set_email(user, new_email):
    if new_email is None:
        raise Exception("Email is null")
    elif len(new_email) > 40:
        raise Exception("Email is too long")
    else:
        user.email = new_email


def get_first_name(user):
    return user.first_name


def set_first_name(user, new_first_name):
    if new_first_name is None:
        raise Exception("First name is null")
    elif len(new_first_name) > 25:
        raise Exception("First name is too long")
    else:
        user.first_name = new_first_name


def get_last_name(user):
    return user.last_name


def set_last_name(user, new_last_name):
    if new_last_name is None:
        raise Exception("First name is null")
    elif len(new_last_name) > 25:
        raise Exception("First name is too long")
    else:
        user.last_name = new_last_name


def get_full_name(user):
    return user.__str__


def get_courses(user):
    return user.course_set.all()


def get_sections(user):
    return user.section_set.all()


def password_check(password, check):
    if password == check:
        return True
    else:
        return False


def exists(username):
    try:
        get_user(username)
        return True
    except:
        return False


def add_user(username, password, role, email, first_name, last_name):
    new_user = User(username=" ", password=" ", email=" ", first_name=" ", last_name=" ")
    try:
        set_username(new_user, username)
        set_password(new_user, password)
        set_role(new_user, role)
        set_email(new_user, email)
        set_first_name(new_user, first_name)
        set_last_name(new_user, last_name)
        new_user.save()
    except Exception as e:
        raise Exception(str(e))


def delete_user(user):
    try:
        user.delete()
    except:
        raise Exception("User doesn't exist")

