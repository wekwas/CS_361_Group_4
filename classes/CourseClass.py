from django.db import models
from SchedulingAPP.models import Course, Semester, WeekDay
from classes import UserClass


def get_all_courses():
    return Course.objects.all()


def get_course(course_name):
    return Course.objects.get(course_name=course_name)


def get_course_name(course):
    return course.course_name


def set_course_name(course, new_course_name):
    if new_course_name is None:
        raise Exception("Course name is null")
    elif len(new_course_name) > 20:
        raise Exception("Course name too long")
    else:
        course.course_name = new_course_name


def get_instructor(course):
    return course.instructor


def set_instructor(course, new_instructor):
    if not UserClass.exists(new_instructor):
        raise Exception("Instructor doesn't exist")
    elif UserClass.get_role(new_instructor) != "Instructor":
        raise Exception("User not Instructor")
    else:
        course.instructor = new_instructor


def get_semester(course):
    return course.semester


def set_semester(course, new_semester):
    if new_semester is None:
        raise Exception("Semester is null")
    elif new_semester != Semester.spring and new_semester != Semester.summer and new_semester != Semester.fall and \
            new_semester != Semester.winter:
        raise Exception("Semester not valid")
    else:
        course.semester = new_semester


def get_days(course):
    return course.days


def get_days_list(course):
    return course.days.split()


def add_day(course, new_day):
    if new_day != WeekDay:
        raise Exception("Day not a WeekDay")
    elif new_day in get_days_list(course):
        return
    else:
        course.days.append(new_day)


def get_time_start(course):
    return course.time_start


def set_time_start(course, new_time):
    if new_time != models.TimeField:
        raise Exception("Start time not valid")
    elif new_time > course.time_end:
        raise Exception("Start time > End time")
    else:
        course.time_start = new_time


def get_time_end(course):
    return course.time_end


def set_time_end(course, new_time):
    if new_time != models.TimeField:
        raise Exception("End time not valid")
    elif new_time < course.time_start:
        raise Exception("End time < Start time")
    else:
        course.time_end = new_time


def exists(course_name):
    try:
        get_course(course_name)
        return True
    except:
        return False


def add_course(course_name, instructor, semester, days, time_start, time_end):
    new_course = Course(course_name=" ", instructor=instructor, days=days, time_start=time_start, time_end=time_end)
    try:
        set_course_name(new_course, course_name)
        set_instructor(new_course, instructor)
        set_semester(new_course, semester)
        for i in days.split():
            add_day(new_course, i)
        set_time_start(new_course, time_start)
        set_time_end(new_course, time_end)
        new_course.save()
    except Exception as e:
        return Exception(str(e))


def delete_course(course):
    try:
        course.delete()
    except:
        raise Exception("Course doesn't exist")

