from django.db import models
from SchedulingAPP.models import Section, WeekDay
from classes import UserClass, CourseClass


def get_section(section_num):
    return Section.objects.get(section_num=section_num)


def get_section_num(section):
    return section.section_num


def set_section_num(section, new_section_num):
    if new_section_num is None:
        raise Exception
    elif not new_section_num.isdigit():
        raise Exception
    elif len(new_section_num) > 3:
        raise Exception
    else:
        section.section_num = new_section_num


def get_ta(section):
    return section.ta


def set_ta(section, new_ta):
    if not UserClass.exists(new_ta):
        raise Exception("User doesn't exist")
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
        raise Exception("new_day not a WeekDay")
    elif new_day in get_days_list(section):
        return
    else:
        section.days.append(new_day)


def get_time_start(section):
    return section.time_start


def set_time_start(section, new_time):
    if new_time != models.TimeField:
        raise Exception("new_time not a TimeField")
    elif new_time > section.time_end:
        raise Exception("new_time > time_end")
    else:
        section.time_start = new_time


def get_time_end(section):
    return section.time_end


def set_time_end(section, new_time):
    if new_time != models.TimeField:
        raise Exception("new_time not a TimeField")
    elif new_time < section.time_start:
        raise Exception("new_time < time_start")
    else:
        section.time_end = new_time


def exists(section_num):
    try:
        Section.objects.get(section_num=section_num)
        return True
    except:
        return False


def add_section(section_num, ta):
    if exists(section_num):
        raise Exception("Section already exists")
    else:
        new_section = Section(section_num=" ", ta=" ")
        try:
            set_section_num(new_section, section_num)
            set_ta(new_section, ta)
            new_section.save()
        except:
            return Exception("Incorrect data")


def delete_section(section_num):
    if exists(section_num):
        Section.objects.get(section_num=section_num).delete()
    else:
        raise Exception("Section doesn't exists")
