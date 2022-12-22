from django.test import TestCase, Client
from .models import User, Course, Section, Notification
from classes import UserClass, CourseClass, SectionClass, NotificationClass


class TestLogin(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        temp = User(username="test_user_TA", password="password_TA", role="TA", email="email_TA",
                    first_name="first_name_TA", last_name="last_name_TA")
        temp.save()
        temp = User(username="test_user_inst", password="password_inst", role="Instructor", email="email_inst",
                    first_name="first_name_inst", last_name="last_name_inst")
        temp.save()
        temp = User(username="test_user_sup", password="password_sup", role="Supervisor", email="email_sup",
                    first_name="first_name_sup", last_name="last_name_sup")
        temp.save()

    def test_nonexistent_user_login(self):
        response = self.monkey.post("/", {"username": "fake_username", "password": "fake_password"}, follow=True)
        self.assertTemplateUsed(response, "LoginPage.html")

    def test_nonexistent_user_message(self):
        response = self.monkey.post("/", {"username": "fake_username", "password": "fake_password"}, follow=True)
        self.assertTemplateUsed(response, "LoginPage.html")
        self.assertIn("Incorrect username", response.context["message"], "message displayed incorrectly with ")

    def test_bad_password_login(self):
        response = self.monkey.post("/", {"username": "test_user_TA", "password": "fake_password"}, follow=True)
        self.assertTemplateUsed(response, "LoginPage.html")

    def test_bad_password_message(self):
        response = self.monkey.post("/", {"username": "test_user_TA", "password": "fake_password"}, follow=True)
        self.assertIn("Incorrect password", response.context["message"], "message displayed incorrectly")

    def test_ta_login(self):
        response = self.monkey.post("/", {"username": "test_user_TA", "password": "password_TA"}, follow=True)
        self.assertRedirects(response, "/TAHomepage/")

    def test_ta_login_template(self):
        response = self.monkey.post("/", {"username": "test_user_TA", "password": "password_TA"}, follow=True)
        self.assertTemplateUsed(response, "TAHomepage.html")

    def test_instructor_login(self):
        response = self.monkey.post("/", {"username": "test_user_inst", "password": "password_inst"}, follow=True)
        self.assertRedirects(response, "/instructorHomepage/")

    def test_instructor_login_template(self):
        response = self.monkey.post("/", {"username": "test_user_inst", "password": "password_inst"}, follow=True)
        self.assertTemplateUsed(response, "instructorHomepage.html")

    def test_supervisor_login(self):
        response = self.monkey.post("/", {"username": "test_user_sup", "password": "password_sup"}, follow=True)
        self.assertRedirects(response, "/supervisorHomepage/")

    def test_supervisor_login_template(self):
        response = self.monkey.post("/", {"username": "test_user_sup", "password": "password_sup"}, follow=True)
        self.assertTemplateUsed(response, "supervisorHomepage.html")


class TestCreateAccount(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        temp = User(username="test_user_TA", password="password_TA", role="TA", email="email_TA",
                    first_name="first_name_TA", last_name="last_name_TA")
        temp.save()
        temp = User(username="test_user_inst", password="password_inst", role="Instructor", email="email_inst",
                    first_name="first_name_inst", last_name="last_name_inst")
        temp.save()
        temp = User(username="test_user_sup", password="password_sup", role="Supervisor", email="email_sup",
                    first_name="first_name_sup", last_name="last_name_sup")
        temp.save()

    def test_default_template(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.get("/CreateAccount/", follow=True)
        self.assertTemplateUsed(response, "CreateAccount.html")

    def test_account_creation(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                                        "username": "test_username", "password": "test_password",
                                                        "passwordCheck": "test_password"}, follow=True)
        self.assertTemplateUsed(response, "CreateAccount.html")
        self.assertTrue(UserClass.exists("test_username"), "user not added")

    def test_account_creation_message(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                                        "username": "test_username", "password": "test_password",
                                                        "passwordCheck": "test_password"}, follow=True)
        self.assertIn("User created", response.context["message"], "message displayed incorrectly")

    def test_new_account_data(self):
        self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                             "username": "test_username", "password": "test_password",
                                             "passwordCheck": "test_password"}, follow=True)
        test_user = User.objects.get(username="test_username")
        self.assertEqual(test_user.username, "test_username", "username incorrect")
        self.assertEqual(test_user.password, "test_password", "password incorrect")
        self.assertEqual(test_user.role, "TA", "role incorrect")
        self.assertEqual(test_user.email, " ", "email incorrect")
        self.assertEqual(test_user.first_name, "test_first_name", "first_name incorrect")
        self.assertEqual(test_user.last_name, "test_last_name", "last_name incorrect")

    def test_duplicate_creation(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "first_name_TA last_name_TA", "role": "TA",
                                                        "username": "test_user_TA", "password": "password_TA",
                                                        "passwordCheck": "password_TA"}, follow=True)
        self.assertTemplateUsed(response, "CreateAccount.html")

    def test_duplicate_creation_message(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "first_name_TA last_name_TA", "role": "TA",
                                                        "username": "test_user_TA", "password": "password_TA",
                                                        "passwordCheck": "password_TA"}, follow=True)
        self.assertIn("Username already exists", response.context["message"], "message displayed incorrectly")

    def test_bad_password(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                                        "username": "test_userName", "password": "test_password",
                                                        "passwordCheck": "fake_password"}, follow=True)
        self.assertFalse(UserClass.exists("test_userName"), "user added")
        self.assertTemplateUsed(response, "CreateAccount.html")

    def test_bad_password_message(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                                        "username": "test_userName", "password": "test_password",
                                                        "passwordCheck": "fake_password"}, follow=True)
        self.assertIn("Passwords don't match", response.context["message"], "message displayed incorrectly")


class TestMyAccount(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        temp = User(username="test_user_TA", password="password_TA", role="TA", email="email_TA",
                    first_name="first_name_TA", last_name="last_name_TA")
        temp.save()
        temp = User(username="test_user_inst", password="password_inst", role="Instructor", email="email_inst",
                    first_name="first_name_inst", last_name="last_name_inst")
        temp.save()
        temp = User(username="test_user_sup", password="password_sup", role="Supervisor", email="email_sup",
                    first_name="first_name_sup", last_name="last_name_sup")
        temp.save()

    def test_default_template(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.get("/MyAccount/", follow=True)
        self.assertTemplateUsed(response, "MyAccount.html")


class TestCreateCourse(TestCase):
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

    def test_default_template(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.get("/CreateCourse/", follow=True)
        self.assertTemplateUsed(response, "CreateCourse.html")

    def test_course_creation(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.post("/CreateCourse/", {"course_name": "test_add_101", "instructor": "test_user_inst",
                                                       "semester": "Winter", "days": "Monday",
                                                       "time_start": "00:01", "time_end": "12:00",
                                                       "location": "the_abyss"}, follow=True)
        self.assertTemplateUsed(response, "CreateCourse.html")
        self.assertTrue(CourseClass.exists("test_add_101"), "course not added")

    def test_course_creation_message(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.post("/CreateCourse/", {"course_name": "test_add_101", "instructor": "test_user_inst",
                                                       "semester": "Winter", "days": "Monday",
                                                       "time_start": "00:01", "time_end": "12:00",
                                                       "location": "the_abyss"}, follow=True)
        self.assertIn("Course created", response.context["message"], "message displayed incorrectly")

    def test_new_course_data(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        self.monkey.post("/CreateCourse/", {"course_name": "test_add_101", "instructor": "test_user_inst",
                                                       "semester": "Winter", "days": "Monday",
                                                       "time_start": "00:01", "time_end": "12:00",
                                                       "location": "the_abyss"}, follow=True)
        test_course = Course.objects.get(course_name="test_add_101")
        self.assertEqual(test_course.course_name, "test_add_101", "course_name incorrect")
        self.assertEqual(test_course.instructor.username, "test_user_inst", "instructor incorrect")
        self.assertEqual(test_course.semester, "Winter", "semester incorrect")
        self.assertEqual(test_course.days, "Monday", "days incorrect")
        self.assertEqual(test_course.time_start, "00:01", "time_start incorrect")
        self.assertEqual(test_course.time_end, "12:00", "time_end incorrect")
        self.assertEqual(test_course.location, "the_abyss", "location incorrect")


class TestViewCourses(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        inst = User(username="test_user_inst", password="password_inst", role="Instructor", email="email_inst",
                    first_name="first_name_inst", last_name="last_name_inst")
        inst.save()

    def test_default_template(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.get("/viewCourses/", follow=True)
        self.assertTemplateUsed(response, "viewCourses.html")


class TestViewAllCourses(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        inst = User(username="test_user_inst", password="password_inst", role="Instructor", email="email_inst",
                    first_name="first_name_inst", last_name="last_name_inst")
        inst.save()

    def test_default_template(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.get("/viewAllCourses/", follow=True)
        self.assertTemplateUsed(response, "viewAllCourses.html")


class TestViewCourse(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        inst = User(username="test_user_inst", password="password_inst", role="Instructor", email="email_inst",
                    first_name="first_name_inst", last_name="last_name_inst")
        inst.save()

    def test_default_template(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.get("/viewCourse/", follow=True)
        self.assertTemplateUsed(response, "viewCourse.html")


class TestCreateSection(TestCase):
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

    def test_default_template(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.get("/CreateLabSection/", follow=True)
        self.assertTemplateUsed(response, "CreateLabSection.html")

    def test_section_creation(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.post("/CreateLabSection/", {"course": "test_course_101", "section_num": "101",
                                                           "ta": "test_user_TA", "days": "Monday",
                                                           "time_start": "00:01", "time_end": "12:00",
                                                           "location": "the_abyss"}, follow=True)
        self.assertTemplateUsed(response, "CreateLabSection.html")
        self.assertTrue(SectionClass.exists("100"), "section not added")

    def test_section_creation_message(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.post("/CreateLabSection/", {"course": "test_course_101", "section_num": "101",
                                                           "ta": "test_user_TA", "days": "Monday",
                                                           "time_start": "00:01", "time_end": "12:00",
                                                           "location": "the_abyss"}, follow=True)
        self.assertIn("Section created", response.context["message"], "message displayed incorrectly")

    def test_new_course_data(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        self.monkey.post("/CreateLabSection/", {"course": "test_course_101", "section_num": "101",
                                                "ta": "test_user_TA", "days": "Monday",
                                                "time_start": "00:01", "time_end": "12:00",
                                                "location": "the_abyss"}, follow=True)
        test_section = Section.objects.get(section_num="101")
        self.assertEqual(test_section.section_num, "101", "course_name incorrect")
        self.assertEqual(test_section.ta.username, "test_user_TA", "instructor incorrect")
        self.assertEqual(test_section.course.course_name, "test_course_101", "semester incorrect")
        self.assertEqual(test_section.days, "Monday", "days incorrect")
        self.assertEqual(test_section.time_start, "00:01", "time_start incorrect")
        self.assertEqual(test_section.time_end, "12:00", "time_end incorrect")
        self.assertEqual(test_section.location, "the_abyss", "location incorrect")


class TestViewSection(TestCase):
    monkey = None

    def setUp(self):
        self.monkey = Client()
        inst = User(username="test_user_inst", password="password_inst", role="Instructor", email="email_inst",
                    first_name="first_name_inst", last_name="last_name_inst")
        inst.save()

    def test_default_template(self):
        session = self.monkey.session
        session['session_username'] = 'test_user_inst'
        session.save()
        response = self.monkey.get("/viewSection/", follow=True)
        self.assertTemplateUsed(response, "viewSection.html")




