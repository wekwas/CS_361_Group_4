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
    else:
        section.section_num = new_section_num


def get_ta(section):
    return section.ta


def set_ta(section, new_ta):
    if not UserClass.exists(new_ta):
        raise Exception("TA doesn't exist")
    elif UserClass.get_role(new_ta) != "TA":
        raise Exception("User not TA")
    else:
        section.ta = new_ta


def get_course(section):
    return section.course


def set_course(section, new_course):
    if not CourseClass.exists(new_course):
        raise Exception("Course doesn't exist")
    else:
        section.course = new_course


def get_days(section):
    return section.days


def get_days_list(section):
    return section.days.split()


def add_day(section, new_day):
    if new_day != WeekDay:
        raise Exception("Day not a WeekDay")
    elif new_day in get_days_list(section):
        return
    else:
        section.days.append(new_day)


def get_time_start(section):
    return section.time_start


def set_time_start(section, new_time):
    if new_time != models.TimeField:
        raise Exception("Start time not valid")
    elif new_time > section.time_end:
        raise Exception("Start time > End time")
    else:
        section.time_start = new_time


def get_time_end(section):
    return section.time_end


def set_time_end(section, new_time):
    if new_time != models.TimeField:
        raise Exception("End time not valid")
    elif new_time < section.time_start:
        raise Exception("End time < Start time")
    else:
        section.time_end = new_time


def get_location(section):
    return section.location


def set_location(section, new_location):
    if new_location is None:
        raise Exception("Location is null")
    elif len(new_location) > 25:
        raise Exception("Location is > 25")
    else:
        section.location = new_location


def exists(section_num):
    try:
        get_section(section_num)
        return True
    except:
        return False


def add_section(section_num, ta, course, days, time_start, time_end, location):
    new_section = Section(section_num=" ", ta=ta, course=course, days="", time_start="00:00", time_end="23:59",
                          location="")
    try:
        set_section_num(new_section, section_num)
        set_ta(new_section, ta)
        set_course(new_section, course)
        for i in days.split():
            add_day(new_section, i)
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
