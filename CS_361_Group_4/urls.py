"""CS_361_Group_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SchedulingAPP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('supervisorHomepage/', SupervisorHomepage.as_view()),
    path('instructorHomepage/', InstructorHomepage.as_view()),
    path('TAHomepage/', TAHomepage.as_view()),
    path('MyAccount/', MyAccount.as_view()),
    path('viewCourses/', ViewCourses.as_view()),
    path('viewAllCourses/', ViewAllCourses.as_view()),
    path('viewAccounts/', ViewAccounts.as_view()),
    path('CreateAccount/', CreateAccount.as_view()),
    path('notification/', Notification.as_view()),
    path('CreateCourse/', CreateCourse.as_view()),
    path('CreateLabSection/', CreateLabSection.as_view()),
    path('newnotification/', NewNotification.as_view()),
    path('viewCourse/', viewCourse.as_view()),
    path('EditCourse/', EditCourse.as_view()),
    path('viewSection/', viewSection.as_view()),










]
