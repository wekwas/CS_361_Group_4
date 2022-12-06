from django.contrib import admin
from .models import User, Course, Section, Notification

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Notification)
