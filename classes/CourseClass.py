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
    if not UserClass.exists(UserClass.get_username(new_instructor)):
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


def set_days(course, new_day):
    if not (new_day in WeekDay):
        raise Exception("Day not a WeekDay")
    course.days = new_day


def get_time_start(course):
    return course.time_start


def set_time_start(course, new_time):
    if new_time is None:
        raise Exception("Start time is null")
    elif len(new_time) > 5:
        raise Exception("Start time > 5")
    else:
        course.time_start = new_time


def get_time_end(course):
    return course.time_end


def set_time_end(course, new_time):
    if new_time is None:
        raise Exception("Start time is null")
    elif len(new_time) > 5:
        raise Exception("End time > 5")
    else:
        course.time_end = new_time


def get_location(course):
    return course.location


def set_location(course, location):
    if location is None:
        raise Exception("Location null")
    elif len(location) > 25:
        raise Exception("Location > 25")
    else:
        course.location = location


def get_sections(course):
    return course.section_set.all()


def get_tas(course):
    tas = []
    for x in get_sections(course):
        tas.append(x.ta)
    return tas


def exists(course_name):
    try:
        get_course(course_name)
        return True
    except:
        return False


def add_course(course_name, instructor, semester, days, time_start, time_end, location):
    new_course = Course(course_name=" ", instructor=instructor, days=days, time_start=time_start, time_end=time_end,
                        location=location)
    try:
        set_course_name(new_course, course_name)
        set_instructor(new_course, instructor)
        set_semester(new_course, semester)
        set_days(new_course, days)
        set_time_start(new_course, time_start)
        set_time_end(new_course, time_end)
        set_location(new_course, location)
        new_course.save()
    except Exception as e:
        raise Exception(str(e))


def delete_course(course):
    try:
        course.delete()
    except:
        raise Exception("Course doesn't exist")

