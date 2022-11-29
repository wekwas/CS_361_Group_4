from django.test import TestCase
from .models import User, Course, Section
from classes import UserClass, CourseClass, SectionClass


class TestUserClass(TestCase):
    def test_default_constructor(self):
        test_user = UserClass.UserClass()
        self.assertEqual(test_user.user.username, " ")
        self.assertEqual(test_user.user.password, " ")
        self.assertEqual(test_user.user.role, "TA")
        self.assertEqual(test_user.user.email, " ")
        self.assertEqual(test_user.user.first_name, " ")
        self.assertEqual(test_user.user.last_name, " ")

    def test_set_username_length(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="username is too long"):
            test_user.set_username("-----------------------------")

    def test_set_username_null(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="username is null"):
            test_user.set_username(None)

    def test_set_password_length(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="password is too long"):
            test_user.set_password("-----------------------------")

    def test_set_password_null(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="password is null"):
            test_user.set_password(None)

    def test_set_role_length(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="role is incorrect"):
            test_user.set_role("-----------------------------")

    def test_set_role_null(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="role is null"):
            test_user.set_role(None)

    def test_set_email_length(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="email is too long"):
            test_user.set_email("----------------------------------------------------")

    def test_set_email_null(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="email is null"):
            test_user.set_email(None)

    def test_set_first_name_length(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="first_name is too long"):
            test_user.set_first_name("-----------------------------")

    def test_set_first_name_null(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="first_name is null"):
            test_user.set_first_name(None)

    def test_set_last_name_length(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="last_name is too long"):
            test_user.set_last_name("-----------------------------")

    def test_set_last_name_null(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="last_name is null"):
            test_user.set_last_name(None)

    def test_add_user(self):
        test_user = UserClass.UserClass()
        test_user.add_user()
        User.objects.get(username=test_user.get_username())

    def test_add_existing_user(self):
        test_user = UserClass.UserClass()
        test_user.add_user()
        test_user2 = UserClass.UserClass()
        with self.assertRaises(Exception, msg="user already in database"):
            test_user2.add_user()

    def test_delete_nonexistent_user(self):
        test_user = UserClass.UserClass()
        with self.assertRaises(Exception, msg="user not in database"):
            test_user.delete_user()

    def test_delete_existing_user(self):
        test_user = UserClass.UserClass()
        test_user.add_user()
        test_user.delete_user()
        with self.assertRaises(Exception, msg="user has been deleted"):
            User.objects.get(username=test_user.get_username())


class TestCourseClass(TestCase):
    def test_default_constructor(self):
        test_course = CourseClass.CourseClass()
        self.assertEqual(test_course.course.course_name, " ")
        self.assertEqual(test_course.course.instructor, " ")
        self.assertEqual(test_course.course.semester, "Fall")

    def test_set_course_name_length(self):
        test_course = CourseClass.CourseClass()
        with self.assertRaises(Exception, msg="course_name is too long"):
            test_course.set_course_name("----------------------------------------------------------")

    def test_set_course_name_null(self):
        test_course = CourseClass.CourseClass()
        with self.assertRaises(Exception, msg="course_name is null"):
            test_course.set_course_name(None)

    def test_set_instructor_length(self):
        test_course = CourseClass.CourseClass()
        with self.assertRaises(Exception, msg="instructor is too long"):
            test_course.set_instructor("-----------------------------------------------------------------------")

    def test_set_instructor_null(self):
        test_course = CourseClass.CourseClass()
        with self.assertRaises(Exception, msg="instructor is null"):
            test_course.set_instructor(None)

    def test_set_semester_length(self):
        test_course = CourseClass.CourseClass()
        with self.assertRaises(Exception, msg="semester is incorrect"):
            test_course.set_semester("-----------------------------")

    def test_set_semester_null(self):
        test_course = CourseClass.CourseClass()
        with self.assertRaises(Exception, msg="semester is null"):
            test_course.set_semester(None)

    def test_add_course(self):
        test_course = CourseClass.CourseClass()
        test_course.add_course()
        Course.objects.get(course_name=test_course.get_course_name())

    def test_add_existing_course(self):
        test_course = CourseClass.CourseClass()
        test_course.add_course()
        test_course2 = CourseClass.CourseClass()
        with self.assertRaises(Exception, msg="Course already in database"):
            test_course2.add_course()

    def test_delete_nonexistent_course(self):
        test_course = CourseClass.CourseClass()
        with self.assertRaises(Exception, msg="Course not in database"):
            test_course.delete_course()

    def test_delete_existing_course(self):
        test_course = CourseClass.CourseClass()
        test_course.add_course()
        test_course.delete_course()
        with self.assertRaises(Exception, msg="Course has been deleted"):
            Course.objects.get(course_name=test_course.get_course_name())


class TestSectionClass(TestCase):
    def test_default_constructor(self):
        test_section = SectionClass.SectionClass()
        self.assertEqual(test_section.section.section_num, " ")
        self.assertEqual(test_section.section.ta, " ")

    def test_set_section_num_length(self):
        test_section = SectionClass.SectionClass()
        with self.assertRaises(Exception, msg="section_num is too long"):
            test_section.set_section_num("----")

    def test_set_section_num_null(self):
        test_section = SectionClass.SectionClass()
        with self.assertRaises(Exception, msg="section_num is null"):
            test_section.set_section_num(None)

    def test_set_ta_length(self):
        test_section = SectionClass.SectionClass()
        with self.assertRaises(Exception, msg="ta is too long"):
            test_section.set_ta("-----------------------------------------------------------------------")

    def test_set_ta_null(self):
        test_section = SectionClass.SectionClass()
        with self.assertRaises(Exception, msg="ta is null"):
            test_section.set_ta(None)

    def test_add_section(self):
        test_section = SectionClass.SectionClass()
        test_section.add_section()
        Section.objects.get(section_num=test_section.get_section_num())

    def test_add_existing_section(self):
        test_section = SectionClass.SectionClass()
        test_section.add_section()
        test_section2 = SectionClass.SectionClass()
        with self.assertRaises(Exception, msg="Section already in database"):
            test_section2.add_section()

    def test_delete_nonexistent_section(self):
        test_section = SectionClass.SectionClass()
        with self.assertRaises(Exception, msg="Section not in database"):
            test_section.delete_section()

    def test_delete_existing_section(self):
        test_section = SectionClass.SectionClass()
        test_section.add_section()
        test_section.delete_section()
        with self.assertRaises(Exception, msg="Section has been deleted"):
            Section.objects.get(section_num=test_section.get_section_num())


class TestLogin(TestCase):
    def test_nonexistent_user_login(self):
        response = self.client.post("/", data={"username": " ", "password": " "}, follow=True)
        self.assertRedirects(response, "/")

    def test_nonexistent_user_message(self):
        response = self.client.post("/", data={"username": " ", "password": " "}, follow=True)
        self.assertRedirects(response, "/")
        self.assertIn("User doesn't exist", response.context["message"], "Error message displayed incorrectly with "
                                                                         "bad password")

    def test_bad_password_login(self):
        test_user = UserClass.UserClass()
        test_user.add_user()
        response = self.client.post("/", data={"username": " ", "password": " "}, follow=True)
        self.assertRedirects(response, "/")

    def test_bad_password_message(self):
        test_user = UserClass.UserClass()
        test_user.add_user()
        response = self.client.post("/", data={"username": " ", "password": " "}, follow=True)
        self.assertIn("Incorrect password", response.context["message"], "Error message displayed incorrectly with "
                                                                         "bad password")

    def test_ta_login(self):
        test_user = UserClass.UserClass()
        test_user.add_user()
        response = self.client.post("/", data={"username": " ", "password": " "})
        self.assertRedirects(response, "/TAHomepage/")

    def test_instructor_login(self):
        test_user = UserClass.UserClass()
        test_user.set_role("Instructor")
        test_user.add_user()
        response = self.client.post("/", data={"username": " ", "password": " "})
        self.assertRedirects(response, "/instructorHomepage/")

    def test_supervisor_login(self):
        test_user = UserClass.UserClass()
        test_user.set_role("Supervisor")
        test_user.add_user()
        response = self.client.post("/", data={"username": " ", "password": " "})
        self.assertRedirects(response, "/supervisorHomepage/")
