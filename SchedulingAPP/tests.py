from django.test import TestCase
from .models import User, Course, Section


class TestUser(TestCase):
    pass


class TestCourse(TestCase):
    pass


class TestSection(TestCase):
    pass


class Login(TestCase):
    def test_login(self):
        test_user = User.objects.create(username="jDoe", password="123", email="generic@email.com", first_name="John"
                                        , last_name="Doe")
        test_user.save()
        response = self.client.post("/", data={"username": "jDoe", "password": "123"})
        self.assertRedirects(response, "/home/")

