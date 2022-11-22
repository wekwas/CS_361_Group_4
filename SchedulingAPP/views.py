from django.shortcuts import render, redirect
from django.views import View
from .models import *


class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        no_such_user = False
        bad_password = False
        try:
            my_user = User.objects.get(username=request.POST['username'])
            bad_password = (my_user.password != request.POST['password'])
        except:
            no_such_user = True
        if no_such_user:
            return render(request, "login.html", {"message": "User doesn't exist"})
        elif bad_password:
            return render(request, "login.html", {"message": "Bad password"})
        else:
            request.session["name"] = my_user.name
            if my_user.role == 'Supervisor':
                return redirect("/supervisorHomepage/")
            elif my_user.role == 'Instructor':
                return redirect("/instructorHomepage/")
            elif my_user.role == 'TA':
                return redirect("/TAHomepage/")

class SupervisorHomepage(View):
    def get(self, request):
        return render(request, "supervisorHomepage.html", {})

    def post(self, request):
        pass

