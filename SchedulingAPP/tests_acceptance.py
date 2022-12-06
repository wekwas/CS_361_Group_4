from django.test import TestCase, Client
from .models import User, Course, Section
from classes import UserClass, CourseClass, SectionClass


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
        response = self.monkey.get("/CreateAccount/", follow=True)
        self.assertTemplateUsed(response, "CreateAccount.html")

    def test_account_creation(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                                        "userName": "test_userName", "password": "test_password",
                                                        "passwordCheck": "test_password"}, follow=True)
        self.assertTemplateUsed(response, "CreateAccount.html")
        self.assertTrue(UserClass.exists("test_userName"), "user not added")

    def test_account_creation_message(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                                        "userName": "test_userName", "password": "test_password",
                                                        "passwordCheck": "test_password"}, follow=True)
        self.assertIn("User created", response.context["message"], "message displayed incorrectly")

    def test_new_account_data(self):
        self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                             "userName": "test_userName", "password": "test_password",
                                             "passwordCheck": "test_password"}, follow=True)
        test_user = User.objects.get(username="test_userName")
        self.assertEqual(test_user.username, "test_userName", "username incorrect")
        self.assertEqual(test_user.password, "test_password", "password incorrect")
        self.assertEqual(test_user.role, "TA", "role incorrect")
        self.assertEqual(test_user.email, " ", "email incorrect")
        self.assertEqual(test_user.first_name, "test_first_name", "first_name incorrect")
        self.assertEqual(test_user.last_name, "test_last_name", "last_name incorrect")

    def test_duplicate_creation(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "first_name_TA last_name_TA", "role": "TA",
                                                        "userName": "test_user_TA", "password": "password_TA",
                                                        "passwordCheck": "password_TA"}, follow=True)
        self.assertTemplateUsed(response, "CreateAccount.html")

    def test_duplicate_creation_message(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "first_name_TA last_name_TA", "role": "TA",
                                                        "userName": "test_user_TA", "password": "password_TA",
                                                        "passwordCheck": "password_TA"}, follow=True)
        self.assertIn("User already exists", response.context["message"], "message displayed incorrectly")

    def test_bad_password(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                                        "userName": "test_userName", "password": "test_password",
                                                        "passwordCheck": "fake_password"}, follow=True)
        self.assertFalse(UserClass.exists("test_userName"), "user added")
        self.assertTemplateUsed(response, "CreateAccount.html")

    def test_bad_password_message(self):
        response = self.monkey.post("/CreateAccount/", {"fullName": "test_first_name test_last_name", "role": "TA",
                                                        "userName": "test_userName", "password": "test_password",
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
        response = self.monkey.get("/MyAccount/", follow=True)
        self.assertTemplateUsed(response, "MyAccount.html")

