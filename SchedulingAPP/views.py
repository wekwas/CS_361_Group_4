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
            my_user = UserClass.get_user(post_username)
            my_password = UserClass.get_password(my_user)
        if not UserClass.password_check(post_password, my_password):
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
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "supervisorHomepage.html", {"role": UserClass.get_role(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "supervisorHomepage.html", {"role": UserClass.get_role(my_user)})


class InstructorHomepage(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "instructorHomepage.html", {"role": UserClass.get_role(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "instructorHomepage.html", {"role": UserClass.get_role(my_user)})


class TAHomepage(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "TAHomepage.html", {"role": UserClass.get_role(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "TAHomepage.html", {"role": UserClass.get_role(my_user)})


class MyAccount(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "MyAccount.html", {"username": UserClass.get_username(my_user),
                                                  "full_name": UserClass.get_full_name(my_user),
                                                  "role": UserClass.get_role(my_user),
                                                  "email": UserClass.get_email(my_user),
                                                  "courses": UserClass.get_courses(my_user),
                                                  "sections": UserClass.get_sections(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "MyAccount.html", {"username": UserClass.get_username(my_user),
                                                  "full_name": UserClass.get_full_name(my_user),
                                                  "role": UserClass.get_role(my_user),
                                                  "email": UserClass.get_email(my_user),
                                                  "courses": UserClass.get_courses(my_user),
                                                  "sections": UserClass.get_sections(my_user)})


class ViewCourses(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewCourses.html", {"role": UserClass.get_role(my_user),
                                                    "courses": UserClass.get_courses(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewCourses.html", {"role": UserClass.get_role(my_user),
                                                    "courses": UserClass.get_courses(my_user)})


class ViewAllCourses(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewAllCourses.html", {"role": UserClass.get_role(my_user),
                                                       "all_courses": CourseClass.get_all_courses()})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewAllCourses.html", {"role": UserClass.get_role(my_user),
                                                       "all_courses": CourseClass.get_all_courses()})


class ViewAccounts(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewAccounts.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users()})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewAccounts.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users()})


class CreateAccount(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "CreateAccount.html", {"username": UserClass.get_username(my_user),
                                                      "role": UserClass.get_role(my_user)})

    def post(self, request):
        full_name = request.POST['fullName'].split()
        role = request.POST['role']
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['passwordCheck']

        if not UserClass.password_check(password, password_check):
            return render(request, "CreateAccount.html", {"message": "Passwords don't match"})
        else:
            try:
                UserClass.add_user(username, password, role, " ", full_name[0], full_name[len(full_name)-1])
            except Exception as e:
                return render(request, "CreateAccount.html", {"message": str(e)})
            return render(request, "CreateAccount.html", {"message": "User created"})

class CreateNotification(View):
    def post(self, request):
        name = request.POST['Name'].split()
        role = request.POST['role']
        message = request.POST['message']

class NewNotification(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "CreateCourse.html", {"username": UserClass.get_username(my_user),
                                                     "full_name": UserClass.get_full_name(my_user),
                                                     "role": UserClass.get_role(my_user),
                                                     "email": UserClass.get_email(my_user),
                                                     "courses": UserClass.get_courses(my_user),
                                                     "sections": UserClass.get_sections(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        name = request.POST["name"]
        time = request.POST["time"]
        date = request.POST["date"]
        message = request.POST["message"]
        role = request.POST["role"]
        email = request.POST["email"]

        try:
            Notification.add_to_class(name, time, date, message, role, email)
        except Exception as e:
            return render(request, "newnotification.html", {"message": str(e)})
        return render(request, "newnotification.html", {"message": "Notification Sent",
                                                     "name": UserClass.get_full_name(my_user),
                                                     "role": UserClass.get_role(my_user),
                                                     "email": UserClass.get_email(my_user),
                                                     "message": UserClass.get(my_user),
                                                     "sections": UserClass.get_sections(my_user)})


...
class notification(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "notification.html", {"username": UserClass.get_username(my_user),
                                                     "full_name": UserClass.get_full_name(my_user),
                                                     "role": UserClass.get_role(my_user),
                                                     "email": UserClass.get_email(my_user),
                                                     "courses": UserClass.get_courses(my_user),
                                                     "sections": UserClass.get_sections(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "notification.html", {"username": UserClass.get_username(my_user),
                                                     "full_name": UserClass.get_full_name(my_user),
                                                     "role": UserClass.get_role(my_user),
                                                     "email": UserClass.get_email(my_user),
                                                     "courses": UserClass.get_courses(my_user),
                                                     "sections": UserClass.get_sections(my_user)})


class CreateLabSection(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "CreateLabSection.html", {"username": UserClass.get_username(my_user),
                                                         "full_name": UserClass.get_full_name(my_user),
                                                         "role": UserClass.get_role(my_user),
                                                         "email": UserClass.get_email(my_user),
                                                         "courses": UserClass.get_courses(my_user),
                                                         "sections": UserClass.get_sections(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        section_num = request.POST["section_num"]
        ta = request.POST["ta"]
        course = request.POST["course"]
        days = request.POST["days"]
        time_start = request.POST["time_start"]
        time_end = request.POST["time_end"]
        try:
            SectionClass.add_section(section_num, ta, course, days, time_start, time_end)
        except Exception as e:
            return render(request, "CreateLabSection.html", {"message": str(e)})
        return render(request, "CreateLabSection.html", {"message": "Section created",
                                                         "username": UserClass.get_username(my_user),
                                                         "full_name": UserClass.get_full_name(my_user),
                                                         "role": UserClass.get_role(my_user),
                                                         "email": UserClass.get_email(my_user),
                                                         "courses": UserClass.get_courses(my_user),
                                                         "sections": UserClass.get_sections(my_user)})
