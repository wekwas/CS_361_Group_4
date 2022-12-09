from django.shortcuts import render, redirect
from django.views import View
from .models import *
from classes import UserClass, CourseClass, SectionClass


class Login(View):
    def get(self, request):
        return render(request, "LoginPage.html", {})

    def post(self, request):
        post_username = request.POST['username']
        post_password = request.POST['password']
        if not UserClass.exists(post_username):
            return render(request, "LoginPage.html", {"message": "Incorrect username"})
        else:
            my_user = User.objects.get(username=post_username)
            my_password = UserClass.get_password(my_user)
        if post_password != my_password:
            return render(request, "LoginPage.html", {"message": "Incorrect password"})
        else:
            request.session["session_username"] = post_username
        if UserClass.get_role(my_user) == 'Supervisor':
            return redirect("/supervisorHomepage/")
        elif UserClass.get_role(my_user) == 'Instructor':
            return redirect("/instructorHomepage/")
        elif UserClass.get_role(my_user) == 'TA':
            return redirect("/TAHomepage/")
        else:
            return render(request, "LoginPage.html", {"message": "User has no role"})


class SupervisorHomepage(View):
    def get(self, request):
        return render(request, "supervisorHomepage.html", {})

    def post(self, request):
        return render(request, "supervisorHomepage.html", {})


class InstructorHomepage(View):
    def get(self, request):
        return render(request, "instructorHomepage.html", {})

    def post(self, request):
        return render(request, "instructorHomepage.html", {})


class TAHomepage(View):
    def get(self, request):
        return render(request, "TAHomepage.html", {})

    def post(self, request):
        return render(request, "TAHomepage.html", {})


class MyAccount(View):
    def get(self, request):
        my_user = User.objects.get(username=request.session["session_username"])
        return render(request, "MyAccount.html", {"username": UserClass.get_username(my_user),
                                                  "full_name": UserClass.get_full_name(my_user),
                                                  "role": UserClass.get_role(my_user),
                                                  "email": UserClass.get_email(my_user)})

    def post(self, request):
        my_user = User.objects.get(username=request.session["session_username"])
        return render(request, "MyAccount.html", {"username": UserClass.get_username(my_user),
                                                  "full_name": UserClass.get_full_name(my_user),
                                                  "role": UserClass.get_role(my_user),
                                                  "email": UserClass.get_email(my_user)})


class ViewCourses(View):
    def get(self, request):
        return render(request, "viewCourses.html", {})

    def post(self, request):
        return render(request, "viewCourses.html", {})


class ViewAllCourses(View):
    def get(self, request):
        return render(request, "viewAllCourses.html", {})

    def post(self, request):
        return render(request, "viewAllCourses.html", {})


class ViewAccounts(View):
    def get(self, request):
        return render(request, "viewAccounts.html", {})

    def post(self, request):
        return render(request, "viewAccounts.html", {})


class CreateAccount(View):
    def get(self, request):
        return render(request, "CreateAccount.html", {})

    def post(self, request):
        fullName = request.POST['fullName'].split()
        role = request.POST['role']
        userName = request.POST['userName']
        password = request.POST['password']
        passwordCheck = request.POST['passwordCheck']

        if UserClass.exists(userName):
            return render(request, "CreateAccount.html", {"message": "User already exists"})
        elif password != passwordCheck:
            return render(request, "CreateAccount.html", {"message": "Passwords don't match"})
        else:
            UserClass.add_user(userName, password, role, " ", fullName[0], fullName[len(fullName)-1])
            return render(request, "CreateAccount.html", {"message": "User created"})


class CreateCourse(View):
    def get(self, request):
        return render(request, "CreateCourse.html", {})

    def post(self, request):
        return render(request, "CreateCourse.html", {})

class notification(View):
    def get(self, request):
        return render(request, "notification.html", {})

    def post(self, request):
        return render(request, "notification.html", {})

class CreateLabSection(View):
    def get(self, request):
        return render(request, "CreateLabSection.html", {})

    def post(self, request):
        return render(request, "CreateLabSection.html", {})
