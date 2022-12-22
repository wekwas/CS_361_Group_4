from django.test import TestCase, Client
from .models import User, Course, Section
from classes import UserClass, CourseClass, SectionClass


class TestUserClass(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        ta = User(username="test_user_TA", password="password_TA", role="TA", email="email_TA",
                  first_name="first_name_TA", last_name="last_name_TA")
        ta.save()
        inst = User(username="test_user_inst", password="password_inst", role="Instructor", email="email_inst",
                    first_name="first_name_inst", last_name="last_name_inst")
        inst.save()
        sup = User(username="test_user_sup", password="password_sup", role="Supervisor", email="email_sup",
                   first_name="first_name_sup", last_name="last_name_sup")
        sup.save()
        course = Course(course_name="test_course_101", instructor=inst, days=" Monday ", time_start="2:00",
                        time_end="3:00", location="location1")
        course.save()
        section = Section(section_num="100", ta=ta, course=course, days=" Monday ", time_start="2:00", time_end="3:00",
                          location="location2")
        section.save()

    def test_get_user(self):
        ta = User.objects.get(username="test_user_TA")
        self.assertEqual(UserClass.get_user("test_user_TA"), ta)

    def test_set_username_length(self):
        ta = UserClass.get_user("test_user_TA")
        with self.assertRaises(Exception, msg="username is too long"):
            UserClass.set_username(ta, "-----------------------------")

    def test_set_username_null(self):
        ta = UserClass.get_user("test_user_TA")
        with self.assertRaises(Exception, msg="username is null"):
            UserClass.set_username(ta, None)

    def test_set_username(self):
        ta = UserClass.get_user("test_user_TA")
        UserClass.set_username(ta, "new_username_ta")
        self.assertEqual("new_username_ta", ta.username)

    def test_set_password_length(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="password is too long"):
            UserClass.set_password(inst, "-----------------------------")

    def test_set_password_null(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="password is null"):
            UserClass.set_password(inst, None)

    def test_set_password(self):
        inst = UserClass.get_user("test_user_inst")
        UserClass.set_password(inst, "new_password_inst")
        self.assertEqual("new_password_inst", inst.password)

    def test_set_nonexistent_role(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="role is incorrect"):
            UserClass.set_role(inst, "-----------------------------")

    def test_set_role_null(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="role is null"):
            UserClass.set_role(inst, None)

    def test_set_role(self):
        inst = UserClass.get_user("test_user_inst")
        UserClass.set_role(inst, "Supervisor")
        self.assertEqual("Supervisor", inst.role)

    def test_set_email_length(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="email is too long"):
            UserClass.set_email(inst, "----------------------------------------------------")

    def test_set_email_null(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="email is null"):
            UserClass.set_email(inst, None)

    def test_set_email(self):
        inst = UserClass.get_user("test_user_inst")
        UserClass.set_email(inst, "new_email_inst")
        self.assertEqual("new_email_inst", inst.email)

    def test_set_first_name_length(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="first_name is too long"):
            UserClass.set_first_name(inst, "-----------------------------")

    def test_set_first_name_null(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="first_name is null"):
            UserClass.set_first_name(inst, None)

    def test_set_first_name(self):
        inst = UserClass.get_user("test_user_inst")
        UserClass.set_first_name(inst, "new_first_name_inst")
        self.assertEqual("new_first_name_inst", inst.first_name)

    def test_set_last_name_length(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="last_name is too long"):
            UserClass.set_last_name(inst, "-----------------------------")

    def test_set_last_name_null(self):
        inst = UserClass.get_user("test_user_inst")
        with self.assertRaises(Exception, msg="last_name is null"):
            UserClass.set_last_name(inst, None)

    def test_set_last_name(self):
        inst = UserClass.get_user("test_user_inst")
        UserClass.set_last_name(inst, "new_last_name_inst")
        self.assertEqual("new_last_name_inst", inst.last_name)

    def test_get_courses(self):
        inst = UserClass.get_user("test_user_inst")
        test_course = Course.objects.get(course_name="test_course_101")
        self.assertEqual(UserClass.get_courses(inst)[0], test_course, msg="course not found")
        with self.assertRaises(Exception, msg="user has no sections"):
            empty = UserClass.get_sections(inst)[0]

    def test_get_sections(self):
        ta = UserClass.get_user("test_user_TA")
        test_section = Section.objects.get(section_num="100")
        self.assertEqual(UserClass.get_sections(ta)[0], test_section, msg="section not found")
        with self.assertRaises(Exception, msg="user has no courses"):
            empty = UserClass.get_courses(ta)[0]

    def test_exists(self):
        self.assertTrue(UserClass.exists("test_user_inst"))

    def test_not_exists(self):
        self.assertFalse(UserClass.exists("fake_username"))

    def test_add_user(self):
        UserClass.add_user("username_new", "password_new", "TA", "email_new", "first_name_new", "last_name_new")
        self.assertTrue(UserClass.exists("username_new"))

    def test_add_existing(self):
        with self.assertRaises(Exception, msg="user already in database"):
            UserClass.add_user("test_user_sup", "password_sup", "Supervisor", "email_sup", "first_name_sup",
                               "last_name_sup")

    def test_delete_user(self):
        inst = UserClass.get_user("test_user_inst")
        UserClass.delete_user(inst)
        self.assertFalse(UserClass.exists("test_user_inst"))

    def test_delete_nonexistent_user(self):
        with self.assertRaises(Exception, msg="user not in database"):
            UserClass.delete_user("fake_username")


class TestCourseClass(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        ta = User(username="test_user_TA", password="password_TA", role="TA", email="email_TA",
                  first_name="first_name_TA", last_name="last_name_TA")
        ta.save()
        inst = User(username="test_user_inst", password="password_inst", role="Instructor", email="email_inst",
                    first_name="first_name_inst", last_name="last_name_inst")
        inst.save()
        course = Course(course_name="test_course_101", instructor=inst, days=" Monday ", time_start="2:00",
                        time_end="3:00", location="location1")
        course.save()
        section = Section(section_num="100", ta=ta, course=course, days=" Monday ", time_start="2:00", time_end="3:00",
                          location="location2")
        section.save()

    def test_get_course(self):
        test_course = Course.objects.get(course_name="test_course_101")
        self.assertEqual(UserClass.get_user("test_user_TA"), ta)


    def test_set_course_name_length(self):
        test_course = Course.objects.get(course_name="test_course_101")
        with self.assertRaises(Exception, msg="course_name is too long"):
            CourseClass.set_course_name(test_course, "-----------------------------")

    def test_set_course_name_null(self):
        test_course = Course.objects.get(course_name="test_course_1")
        with self.assertRaises(Exception, msg="course_name is null"):
            CourseClass.set_course_name(test_course, None)

    def test_set_course_name(self):
        test_course = Course.objects.get(course_name="test_course_1")
        CourseClass.set_course_name(test_course, "new_course_name")
        self.assertEqual("new_course_name", test_course.course_name)

    def test_set_instructor_length(self):
        test_course = Course.objects.get(course_name="test_course_2")
        with self.assertRaises(Exception, msg="instructor is too long"):
            CourseClass.set_instructor(test_course, "----------------------------------------------------------")

    def test_set_instructor_null(self):
        test_course = Course.objects.get(course_name="test_course_2")
        with self.assertRaises(Exception, msg="instructor is null"):
            CourseClass.set_instructor(test_course, None)

    def test_set_instructor(self):
        test_course = Course.objects.get(course_name="test_course_2")
        CourseClass.set_instructor(test_course, "new_instructor")
        self.assertEqual("new_instructor", test_course.instructor)

    def test_set_nonexistent_semester(self):
        test_course = Course.objects.get(course_name="test_course_2")
        with self.assertRaises(Exception, msg="semester is incorrect"):
            CourseClass.set_semester(test_course, "-----------------------------")

    def test_set_semester_null(self):
        test_course = Course.objects.get(course_name="test_course_2")
        with self.assertRaises(Exception, msg="semester is null"):
            CourseClass.set_semester(test_course, None)

    def test_set_semester(self):
        test_course = Course.objects.get(course_name="test_course_2")
        CourseClass.set_semester(test_course, "Summer")
        self.assertEqual("Summer", test_course.semester)

    def test_exists(self):
        self.assertTrue(CourseClass.exists("test_course_2"))

    def test_not_exists(self):
        self.assertFalse(CourseClass.exists("fake_course_name"))

    def test_add_course(self):
        CourseClass.add_course("course_name_new", "instructor_new", "Summer")
        self.assertTrue(CourseClass.exists("course_name_new"))

    def test_add_existing(self):
        with self.assertRaises(Exception, msg="course already in database"):
            CourseClass.add_course("test_course_2", "instructor_new", "Summer")

    def test_delete_course(self):
        CourseClass.delete_course("test_course_2")
        self.assertFalse(CourseClass.exists("test_course_2"))

    def test_delete_nonexistent_course(self):
        with self.assertRaises(Exception, msg="course not in database"):
            CourseClass.delete_course("fake_course_name")


class TestSectionClass(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        temp = Section(section_num="123", ta="test_ta_1")
        temp.save()
        temp = Section(section_num="456", ta="test_ta_2")
        temp.save()
        temp = Section(section_num="789", ta="test_ta_3",)
        temp.save()

    def test_set_section_num_length(self):
        test_section = Section.objects.get(section_num="123")
        with self.assertRaises(Exception, msg="course_name is too long"):
            SectionClass.set_section_num(test_section, "-----------------------------")

    def test_set_section_num_null(self):
        test_section = Section.objects.get(section_num="123")
        with self.assertRaises(Exception, msg="course_name is null"):
            SectionClass.set_section_num(test_section, None)

    def test_set_section_num(self):
        test_section = Section.objects.get(section_num="123")
        SectionClass.set_section_num(test_section, "321")
        self.assertEqual("321", test_section.section_num)

    def test_set_ta_length(self):
        test_section = Section.objects.get(section_num="456")
        with self.assertRaises(Exception, msg="ta is too long"):
            SectionClass.set_ta(test_section, "----------------------------------------------------------")

    def test_set_ta_null(self):
        test_section = Section.objects.get(section_num="456")
        with self.assertRaises(Exception, msg="ta is null"):
            SectionClass.set_ta(test_section, None)

    def test_set_ta(self):
        test_section = Section.objects.get(section_num="456")
        SectionClass.set_ta(test_section, "new_ta")
        self.assertEqual("new_ta", test_section.ta)

    def test_exists(self):
        self.assertTrue(SectionClass.exists("456"))

    def test_not_exists(self):
        self.assertFalse(SectionClass.exists("999"))

    def test_add_course(self):
        SectionClass.add_section("999", "ta_new")
        self.assertTrue(SectionClass.exists("999"))

    def test_add_existing(self):
        with self.assertRaises(Exception, msg="section already in database"):
            SectionClass.add_section("456", "ta_new")

    def test_delete_course(self):
        SectionClass.delete_section("456")
        self.assertFalse(SectionClass.exists("456"))

    def test_delete_nonexistent_course(self):
        with self.assertRaises(Exception, msg="section not in database"):
            SectionClass.delete_section("999")