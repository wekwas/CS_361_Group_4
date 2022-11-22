from django.test import TestCase
from .models import User, Course, Section


class TestUser(TestCase):
    def test_default_constructor(self):
        with self.assertRaises(Exception, msg="Default constructor fails to raise exception"):
            m = User()
            m.full_clean()

    def test_default_userType(self):
        m = User(username="jDoe", password="123", email="generic@email.com", first_name="John", last_name="Doe")
        self.assertEqual("TA", m.userType, msg="Default userType not TA")
        m.full_clean()

    def test_long_args(self):
        with self.assertRaises(Exception, msg="name is too long (>25)"):
            m = User(username="--------------------------", password="123", email="generic@email.com", first_name="John", last_name="Doe")
            m.full_clean()

        with self.assertRaises(Exception, msg="password is too long (>25)"):
            m = User(username="jDoe", password="--------------------------", email="generic@email.com", first_name="John", last_name="Doe")
            m.full_clean()

        with self.assertRaises(Exception, msg="userType is too long (>10)"):
            m = User(username="jDoe", password="123", userType="--------------------------", email="generic@email.com", first_name="John", last_name="Doe")
            m.full_clean()

        with self.assertRaises(Exception, msg="email is too long (>40)"):
            m = User(username="jDoe", password="123", email="----------------------------------------------------",
                     first_name="John", last_name="Doe")
            m.full_clean()

        with self.assertRaises(Exception, msg="first_name is too long (>25)"):
            m = User(username="jDoe", password="123", email="generic@email.com", first_name="--------------------------", last_name="Doe")
            m.full_clean()

        with self.assertRaises(Exception, msg="last_name is too long (>25)"):
            m = User(username="jDoe", password="123", email="generic@email.com", first_name="John", last_name="--------------------------")
            m.full_clean()

    def test_null_args(self):
        with self.assertRaises(Exception, msg="name is null"):
            test_user = User(username=None, password="123", email="generic@email.com", first_name="John", last_name="Doe")
            test_user.full_clean()

        with self.assertRaises(Exception, msg="password is null"):
            test_user = User(username="jDoe", password=None, email="generic@email.com", first_name="John", last_name="Doe")
            test_user.full_clean()

        with self.assertRaises(Exception, msg="userType is too null"):
            test_user = User(username="jDoe", password="123", userType=None, email="generic@email.com", first_name="John", last_name="Doe")
            test_user.full_clean()

        with self.assertRaises(Exception, msg="email is null"):
            test_user = User(username="jDoe", password="123", email=None, first_name="John", last_name="Doe")
            test_user.full_clean()

        with self.assertRaises(Exception, msg="first_name is null"):
            test_user = User(username="jDoe", password="123", email="generic@email.com", first_name=None, last_name="Doe")
            test_user.full_clean()

        with self.assertRaises(Exception, msg="last_name is null"):
            test_user = User(username="jDoe", password="123", email="generic@email.com", first_name="John", last_name=None)
            test_user.full_clean()

    def test_str(self):
        test_user = User(username="jDoe", password="123", email="generic@email.com", first_name="John", last_name="Doe")
        self.assertEqual(test_user.__str__(), "John Doe")


class TestCourse(TestCase):
    def test_default_constructor(self):
        with self.assertRaises(Exception, msg="Default constructor fails to raise exception"):
            test_course = Course()
            test_course.full_clean()

    def test_default_semester(self):
        test_course = Course(course_name="CS 361", instructor="Jayson Rock")
        self.assertEqual("Fall", test_course.semester, msg="Default semester not Fall")
        test_course.full_clean()

    def test_long_args(self):
        with self.assertRaises(Exception, msg="course_name is too long (>25)"):
            test_course = Course(course_name="--------------------------", instructor="Jayson Rock")
            test_course.full_clean()

        with self.assertRaises(Exception, msg="instructor is too long (>50)"):
            test_course = Course(course_name="CS 361", instructor="--------------------------------------------"
                                                                  "--------")
            test_course.full_clean()

    def test_null_args(self):
        with self.assertRaises(Exception, msg="course_name is null"):
            test_course = Course(course_name=None, instructor="Jayson Rock")
            test_course.full_clean()

        with self.assertRaises(Exception, msg="instructor is null"):
            test_course = Course(course_name="CS 361", instructor=None)
            test_course.full_clean()

    def test_str(self):
        test_course = Course(course_name="CS 361", instructor="Jayson Rock")
        self.assertEqual(test_course.__str__(), "CS 361")


class TestSection(TestCase):
    def test_default_constructor(self):
        with self.assertRaises(Exception, msg="Default constructor fails to raise exception"):
            test_section = Course()
            test_section.full_clean()

    def test_long_args(self):
        with self.assertRaises(Exception, msg="ta is too long (>50)"):
            test_section = Section(section_num=101, ta="--------------------------------------------"
                                                       "--------")
            test_section.full_clean()

    def test_null_args(self):
        with self.assertRaises(Exception, msg="section_num is null"):
            test_section = Section(section_num=None, ta="Jayson Rock")
            test_section.full_clean()

        with self.assertRaises(Exception, msg="ta is null"):
            test_section = Section(section_num=101, ta=None)
            test_section.full_clean()

    def test_str(self):
        test_section = Section(section_num=101, ta="Jayson Rock")
        self.assertEqual(test_section.__str__(), "101")


class TestLogin(TestCase):
    def test_login(self):
        test_user = User.objects.create(username="jDoe", password="123", email="generic@email.com", first_name="John"
                                        , last_name="Doe")
        test_user.save()
        response = self.client.post("/", data={"username": "jDoe", "password": "123"})
        self.assertRedirects(response, "/TAHomepage/")


class TestUrlExists(TestCase):
    def test_login_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200, "/ doesn't exist")



