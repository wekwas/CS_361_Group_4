from SchedulingAPP.models import Notification, Role


def get_name(name):
    return Notification.name


def set_name(notification,new_name):
    if new_name is None:
        raise Exception("Name is null")
    elif len(new_name) > 50:
        raise Exception("name is too long")
    else:
        notification.name = new_name;


def get_message(message):
    return Notification.name


def set_message(notification, new_message):
    if new_message is None:
        raise Exception("Message is null")
    elif len(new_message) > 500:
        raise Exception("Message is too long")
    else:
        notification.message=new_message


def get_email(email):
    return Notification.email


def set_email(notification, new_email):
    if new_email is None:
        raise Exception("Email is null")
    elif len(new_email) > 60:
        raise Exception("Email is too long")
    else:
        notification.email=new_email


def add_notification(name, message, email,role):
    new_notification = Notification(name="", message="", email="")



    try:

        set_message(new_notification,message)
        set_name(new_notification,name)
        set_email(new_notification,email)
        set_role(new_notification,role)
    except Exception as e:
        return Exception(str(e))


def get_role(user):
    return user.role


def set_role(notification, new_role):
    if new_role is None:
        raise Exception("Role is null")
    elif new_role != Role.supervisor and new_role != Role.instructor and new_role != Role.ta:
        raise Exception("Role not valid")
    else:
        notification.role = new_role


def get_allnotifications():
    return Notification.objects.all()



