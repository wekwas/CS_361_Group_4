from SchedulingAPP.models import Course, Semester
from classes import UserClass


def get_course(course_name):
    return Course.objects.get(course_name=course_name)


def get_course_name(course):
    return course.course_name


def set_course_name(course, new_course_name):
    if new_course_name is None:
        raise Exception
    elif len(new_course_name) > 20:
        raise Exception
    else:
        course.course_name = new_course_name


def get_instructor(course):
    return course.instructor


def set_instructor(course, new_instructor):
    if not UserClass.exists(new_instructor):
        raise Exception("User doesn't exist")
    elif UserClass.get_role(new_instructor) != "Instructor":
        raise Exception("User not Instructor")
    else:
        course.instructor = new_instructor


def get_semester(course):
    return course.semester


def set_semester(course, new_semester):
    if new_semester is None:
        raise Exception
    elif new_semester != Semester.spring and new_semester != Semester.summer and new_semester != Semester.fall and \
            new_semester != Semester.winter:
        raise Exception
    else:
        course.semester = new_semester


def exists(course_name):
    try:
        get_course(course_name)
        return True
    except:
        return False


def add_course(course_name, instructor, semester):
    if not UserClass.exists(instructor):
        raise Exception("User doesn't exist")
    new_course = Course(course_name=" ", instructor=instructor)
    try:
        set_course_name(new_course, course_name)
        set_instructor(new_course, instructor)
        set_semester(new_course, semester)
        new_course.save()
    except Exception as e:
        return Exception(str(e))


def delete_course(course):
    course.delete()

