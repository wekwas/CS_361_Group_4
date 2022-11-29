from django.shortcuts import render, redirect
from django.views import View
from .models import *


class Login(View):
    def get(self, request):
        return render(request, "LoginPage.html", {})

    def post(self, request):
        no_such_user = False
        bad_password = False
        try:
            my_user = User.objects.get(username=request.POST['username'])
            bad_password = (my_user.password != request.POST['password'])
        except:
            no_such_user = True
        if no_such_user:
            return render(request, "LoginPage.html", {"message": "User doesn't exist"})
        elif bad_password:
            return render(request, "LoginPage.html", {"message": "Incorrect password"})
        else:
            request.session["username"] = my_user.username
            if my_user.role == 'Supervisor':
                return redirect("/supervisorHomepage/")
            elif my_user.role == 'Instructor':
                return redirect("/instructorHomepage/")
            elif my_user.role == 'TA':
                return redirect("/TAHomepage/")
            else:
                return render(request, "LoginPage.html", {"message": "User doesn't have a role"})


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
