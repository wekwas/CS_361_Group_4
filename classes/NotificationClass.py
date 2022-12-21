from SchedulingAPP.models import Notification

def get_name(name):
    return Notification.objects.get(name=name)

