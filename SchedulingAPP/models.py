from django.db import models


class WeekDay(models.TextChoices):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Monday_Wednesday = "Monday Wednesday"
    Monday_Wednesday_Friday = "Monday Wednesday Friday"
    Tuesday_Thursday = "Tuesday Thursday"


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
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.ta)
    email = models.CharField(max_length=40)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Course(models.Model):
    course_name = models.CharField(max_length=20)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10, choices=Semester.choices, default=Semester.fall)
    days = models.CharField(max_length=23, choices=WeekDay.choices, default=WeekDay.Monday)
    time_start = models.CharField(max_length=5)
    time_end = models.CharField(max_length=5)
    location = models.CharField(max_length=25)

    def __str__(self):
        return self.course_name


class Section(models.Model):
    section_num = models.CharField(max_length=3)
    ta = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    days = models.CharField(max_length=23, choices=WeekDay.choices, default=WeekDay.Monday)
    time_start = models.CharField(max_length=5)
    time_end = models.CharField(max_length=5)
    location = models.CharField(max_length=25)

    def __str__(self):
        return "%d" % self.section_num


class Notification(models.Model):
    name = models.CharField(max_length=25)
    time = models.TimeField()
    date = models.DateField()
    message = models.CharField(max_length=500)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.ta)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.name

