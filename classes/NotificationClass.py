from SchedulingAPP.models import Notification


def get_name(name):
    return Notification.objects.get(name=name)

def get_email(email):
    return Notification.objects.get(email=email)

def get_message(message):
    return Notification.objects.get(message=message)

def get_role(user):
    return user.role