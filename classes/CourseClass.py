from SchedulingAPP.models import Course, Semester


class CourseClass:
    def __init__(self):
        self.course = Course(course_name=" ", instructor=" ")

    def get_course_name(self):
        return self.course.course_name

    def set_course_name(self, new_course_name):
        if new_course_name is None:
            raise Exception
        elif len(new_course_name) > 20:
            raise Exception
        else:
            self.course.course_name = new_course_name

    def get_instructor(self):
        return self.course.instructor

    def set_instructor(self, new_instructor):
        if new_instructor is None:
            raise Exception
        elif len(new_instructor) > 50:
            raise Exception
        else:
            self.course.instructor = new_instructor

    def get_semester(self):
        return self.course.semester

    def set_semester(self, new_semester):
        if new_semester is None:
            raise Exception
        elif new_semester != Semester.spring and new_semester != Semester.summer and new_semester != Semester.fall and \
                new_semester != Semester.winter:
            raise Exception
        else:
            self.course.semester = new_semester

    def add_course(self):
        try:
            Course.objects.get(course_name=self.course.course_name)
        except:
            self.course.save()
            return
        raise Exception

    def delete_course(self):
        self.course.delete()

