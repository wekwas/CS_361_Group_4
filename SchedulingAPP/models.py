from django.db import models


class Role(models.TextChoices):
    supervisor = "Supervisor"
    instructor = "Instructor"
    ta = "TA"


class Semester(models.TextChoices):
    spring = "Spring"
    fall = "Fall"
    summer = "Summer"
    winter = "Winter"


class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    userType = models.CharField(max_length=10, choices=Role.choices, default=Role.ta)
    email = models.CharField(max_length=40)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)


class Course(models.Model):
    course_name = models.CharField(max_length=20)
    instructor = models.CharField(max_length=50)
    semester = models.CharField(max_length=10, choices=Semester.choices, default=Semester.fall)


class Section(models.Model):
    section_num = models.IntegerField()
    ta = models.CharField(max_length=50)

