from django.db import models
from SchedulingAPP.models import Section, WeekDay
from classes import UserClass, CourseClass


def get_section(section_num):
    return Section.objects.get(section_num=section_num)


def get_section_num(section):
    return section.section_num


def set_section_num(section, new_section_num):
    if new_section_num is None:
        raise Exception("Section number is null")
    elif not new_section_num.isdigit():
        raise Exception("Section number not a number")
    elif len(new_section_num) > 3:
        raise Exception("Section number too large")
    elif exists("new_section_num"):
        raise Exception("Section num already in use")
    else:
        section.section_num = new_section_num
        section.save()


def get_ta(section):
    return section.ta


def set_ta(section, new_ta):
    if not UserClass.exists(UserClass.get_username(new_ta)):
        raise Exception("TA doesn't exist")
    elif UserClass.get_role(new_ta) != "TA":
        raise Exception("User not TA")
    else:
        section.ta = new_ta
        section.save()


def get_course(section):
    return section.course


def set_course(section, new_course):
    if not CourseClass.exists(new_course):
        raise Exception("Course doesn't exist")
    else:
        section.course = new_course
        section.save()


def get_days(section):
    return section.days


def set_days(section, new_day):
    if not (new_day in WeekDay):
        raise Exception("Day not a WeekDay")
    section.days = new_day
    section.save()


def get_time_start(section):
    return section.time_start


def set_time_start(section, new_time):
    if new_time is None:
        raise Exception("Start time not null")
    elif len(new_time) > 5:
        raise Exception("Start time > 5")
    else:
        section.time_start = new_time
        section.save()


def get_time_end(section):
    return section.time_end


def set_time_end(section, new_time):
    if new_time is None:
        raise Exception("Start time not null")
    elif len(new_time) > 5:
        raise Exception("End time > 5")
    else:
        section.time_end = new_time
        section.save()


def get_location(section):
    return section.location


def set_location(section, location):
    if location is None:
        raise Exception("Location null")
    elif len(location) > 25:
        raise Exception("Location > 25")
    else:
        section.location = location
        section.save()


def exists(section_num):
    try:
        get_section(section_num)
        return True
    except:
        return False


def add_section(section_num, ta, course, days, time_start, time_end, location):
    new_section = Section(section_num=" ", ta=ta, course=course, days="", time_start="00:00", time_end="23:59")
    try:
        set_section_num(new_section, section_num)
        set_ta(new_section, ta)
        set_course(new_section, course)
        set_days(new_section, days)
        set_time_start(new_section, time_start)
        set_time_end(new_section, time_end)
        set_location(new_section, location)
        new_section.save()
    except Exception as e:
        return Exception(str(e))


def delete_section(section):
    try:
        section.delete()
    except:
        raise Exception("Section doesn't exist")
