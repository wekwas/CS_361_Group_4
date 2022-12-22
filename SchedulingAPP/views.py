from django.shortcuts import render, redirect
from django.views import View
from .models import *
from classes import UserClass, CourseClass, SectionClass, NotificationClass
from datetime import datetime


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
        return render(request, "supervisorHomepage.html", {"role": UserClass.get_role(my_user),
                                                           "first_name": UserClass.get_first_name(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "supervisorHomepage.html", {"role": UserClass.get_role(my_user)})


class InstructorHomepage(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "instructorHomepage.html", {"role": UserClass.get_role(my_user),
                                                           "first_name": UserClass.get_first_name(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "instructorHomepage.html", {"role": UserClass.get_role(my_user)})


class TAHomepage(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "TAHomepage.html", {"role": UserClass.get_role(my_user),
                                                   "first_name": UserClass.get_first_name(my_user)})

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
        return render(request, "editSelfAccount.html", {"username": UserClass.get_username(my_user),
                                                        "account": my_user,
                                                        "role": UserClass.get_role(my_user)})


class ViewCourses(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewCourses.html", {"role": UserClass.get_role(my_user),
                                                    "courses": UserClass.get_courses(my_user),
                                                    "tacourses": UserClass.get_sections((my_user))})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        reqcourse = CourseClass.get_course(request.POST['coursesub'])
        labs = CourseClass.get_sections(reqcourse)
        return render(request, "viewCourse.html", {"role": UserClass.get_role(my_user),
                                                   "course": reqcourse,
                                                   "labs": labs})


class ViewAllCourses(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewAllCourses.html", {"role": UserClass.get_role(my_user),
                                                       "all_courses": CourseClass.get_all_courses()})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        reqcourse = CourseClass.get_course(request.POST['coursesub'])
        labs = CourseClass.get_sections(reqcourse)
        return render(request, "viewCourse.html", {"role": UserClass.get_role(my_user),
                                                   "course": reqcourse,
                                                   "labs": labs})


class ViewAccounts(View):
    def get(self, request):
        talist = UserClass.get_all_tas()
        instlist = UserClass.get_all_instructors()
        suplist = UserClass.get_all_supervisors()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewAccounts.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users(),
                                                     "supervisors": suplist,
                                                     "instructors": instlist,
                                                     "tas": talist})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        account = UserClass.get_user(request.POST['account'])
        courses = UserClass.get_courses(account)
        labs = UserClass.get_sections(account)
        return render(request, "viewTargetAccount.html", {"role": UserClass.get_role(my_user),
                                                          "account": account,
                                                          "courses": courses,
                                                          "labs": labs})


class CreateAccount(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "CreateAccount.html", {"username": UserClass.get_username(my_user),
                                                      "role": UserClass.get_role(my_user)})

    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
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
            return render(request, "CreateAccount.html", {"message": "User created",
                                                          "role": UserClass.get_role(my_user)})


class NewNotification(View):
    def get(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "newnotification.html", {"name": NotificationClass.get_name(my_user),
                                                        "role": UserClass.get_role(my_user),
                                                        "email": UserClass.get_email(my_user)})

    def post(self, request):

        my_user = UserClass.get_user(request.session["session_username"])
        name = request.POST["name"]
        message = request.POST["message"]
        email = request.POST["email"]


        try:
            NotificationClass.add_notification(name, message, email)
        except Exception as e:
            return render(request, "newnotification.html", {"message": str(e)})
        return render(request, "newnotification.html", {"message": "Notification Sent",
                                                        "name": UserClass.get_full_name(my_user),
                                                        "role": UserClass.get_role(my_user),
                                                        "email": UserClass.get_email(my_user)})


...
class Notification(View):
    def get(self, request):
        all_notifications = NotificationClass.get_allnotifications();
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "notification.html", {"name": NotificationClass.get_name(Notification),
                                                     "full_name": UserClass.get_full_name(my_user),
                                                     "role": UserClass.get_role(my_user),
                                                     "email": UserClass.get_email(my_user),
                                                     "courses": UserClass.get_courses(my_user),
                                                     "sections": UserClass.get_sections(my_user),
                                                     "all_notifications": all_notifications})


class CreateLabSection(View):
    def get(self, request):
        talist = UserClass.get_all_tas()
        courses = CourseClass.get_all_courses()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "CreateLabSection.html", {"role": UserClass.get_role(my_user),
                                                         "tas": talist,
                                                         "courses": courses})

    def post(self, request):
        talist = UserClass.get_all_tas()
        courses = CourseClass.get_all_courses()
        my_user = UserClass.get_user(request.session["session_username"])
        section_num = request.POST["section_num"]
        ta_name = request.POST["ta"]
        course = CourseClass.get_course(request.POST["course"])
        days = request.POST["days"]
        time_start = request.POST["time_start"]
        time_end = request.POST["time_end"]
        location = request.POST["location"]
        ta = UserClass.get_user(ta_name)
        try:
            SectionClass.add_section(section_num, ta, course, days, time_start, time_end, location)
        except Exception as e:
            return render(request, "CreateLabSection.html", {"message": str(e)})
        return render(request, "CreateLabSection.html", {"message": "Section created",
                                                         "role": UserClass.get_role(my_user),
                                                         "tas": talist,
                                                         "courses": courses})


class CreateCourse(View):
    def get(self, request):
        instlist = UserClass.get_all_instructors()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "CreateCourse.html", {"role": UserClass.get_role(my_user),
                                                     "Instructors": instlist})

    def post(self, request):
        instlist = UserClass.get_all_instructors()
        my_user = UserClass.get_user(request.session["session_username"])
        course_name = request.POST["course_name"]
        if not UserClass.get_all_instructors:
            return render(request, "CreateCourse.html", {"message": "No instructor"})
        instructor_name = request.POST["instructor"]
        semester = request.POST["semester"]
        days = request.POST["days"]
        time_start = request.POST["time_start"]
        time_end = request.POST["time_end"]
        location = request.POST["location"]
        instructor = UserClass.get_user(instructor_name)
        try:
            CourseClass.add_course(course_name, instructor, semester, days, time_start, time_end, location)
        except Exception as e:
            return render(request, "CreateCourse.html", {"message": str(e)})
        return render(request, "CreateCourse.html", {"message": "Course created",
                                                     "role": UserClass.get_role(my_user),
                                                     "Instructors": instlist})
class viewCourse(View):
    def get(self, request):
        talist = UserClass.get_all_tas()
        instlist = UserClass.get_all_instructors()
        suplist = UserClass.get_all_supervisors()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewCourse.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users(),
                                                     "supervisors": suplist,
                                                     "instructors": instlist,
                                                     "tas": talist})
    def post(self, request):

        my_user = UserClass.get_user(request.session["session_username"])

        try:
            reqcourse = CourseClass.get_course(request.POST['coursesub'])
            return render(request, "editCourse.html", {"role": UserClass.get_role(my_user),
                                                       "course": reqcourse,
                                                       "Instructors": UserClass.get_all_instructors()})
        except Exception as e:
            reqsec = SectionClass.get_section(request.POST['secsub'])
            return render(request, "viewSection.html", {"role": UserClass.get_role(my_user),
                                                        "sec": reqsec})
class EditCourse(View):
    def get(self, request):
        talist = UserClass.get_all_tas()
        instlist = UserClass.get_all_instructors()
        suplist = UserClass.get_all_supervisors()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewCourse.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users(),
                                                     "supervisors": suplist,
                                                     "instructors": instlist,
                                                     "tas": talist})
    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        courseobj = CourseClass.get_course(request.POST["coursesub"])
        course_name = request.POST["course_name"]
        instructor_name = request.POST["instructor"]
        semester = request.POST["semester"]
        days = request.POST["days"]
        time_start = request.POST["time_start"]
        time_end = request.POST["time_end"]
        location = request.POST["location"]
        instructor = UserClass.get_user(instructor_name)
        try:
            CourseClass.set_course_name(courseobj, course_name)
            CourseClass.set_days(courseobj, days)
            CourseClass.set_semester(courseobj, semester)
            CourseClass.set_time_start(courseobj, time_start)
            CourseClass.set_time_end(courseobj, time_end)
            CourseClass.set_location(courseobj, location)
            CourseClass.set_instructor(courseobj, instructor)
        except Exception as e:
            return render(request, "EditCourse.html", {"message": str(e),
                                                       "role": UserClass.get_role(my_user),
                                                       "course": courseobj,
                                                       "Instructors": UserClass.get_all_instructors()})
        return render(request, "ViewCourse.html", {"role": UserClass.get_role(my_user),
                                                   "course": courseobj,
                                                   "labs": CourseClass.get_sections(courseobj)})

class viewSection(View):
    def get(self, request):
        talist = UserClass.get_all_tas()
        instlist = UserClass.get_all_instructors()
        suplist = UserClass.get_all_supervisors()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewSection.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users(),
                                                     "supervisors": suplist,
                                                     "instructors": instlist,
                                                     "tas": talist})
    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        reqsec = SectionClass.get_section(request.POST['secsub'])
        return render(request, "editSection.html", {"role": UserClass.get_role(my_user),
                                                   "sec": reqsec,
                                                   "tas": UserClass.get_all_tas()})

class editSection(View):
    def get(self, request):
        talist = UserClass.get_all_tas()
        instlist = UserClass.get_all_instructors()
        suplist = UserClass.get_all_supervisors()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewCourse.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users(),
                                                     "supervisors": suplist,
                                                     "instructors": instlist,
                                                     "tas": talist})
    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        secobj = SectionClass.get_section(request.POST["secsub"])
        section_num = request.POST["section_num"]
        taname = request.POST["ta"]
        days = request.POST["days"]
        time_start = request.POST["time_start"]
        time_end = request.POST["time_end"]
        location = request.POST["location"]
        ta = UserClass.get_user(taname)
        try:
            SectionClass.set_section_num(secobj,section_num)
            SectionClass.set_time_start(secobj, time_start)
            SectionClass.set_time_end(secobj,time_end)
            SectionClass.set_days(secobj,days)
            SectionClass.set_location(secobj,location)
            SectionClass.set_ta(secobj,ta)
        except Exception as e:
            return render(request, "editSection.html", {"message": str(e),
                                                        "role": UserClass.get_role(my_user),
                                                        "sec": secobj,
                                                        "tas": UserClass.get_all_tas()})
        return render(request, "viewSection.html", {"role": UserClass.get_role(my_user),
                                                    "sec": secobj})

class viewTargetAccount(View):


    def get(self, request):

        talist = UserClass.get_all_tas()
        instlist = UserClass.get_all_instructors()
        suplist = UserClass.get_all_supervisors()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewCourse.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users(),
                                                     "supervisors": suplist,
                                                     "instructors": instlist,
                                                     "tas": talist})
    def post(self, request):

        my_user = UserClass.get_user(request.session["session_username"])
        account = UserClass.get_user(request.POST['account'])
        return render(request, "editTargetAccount.html", {"role": UserClass.get_role(my_user),
                                                          "account": account})

class editTargetAccount(View):
    def get(self, request):
        talist = UserClass.get_all_tas()
        instlist = UserClass.get_all_instructors()
        suplist = UserClass.get_all_supervisors()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "viewCourse.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users(),
                                                     "supervisors": suplist,
                                                     "instructors": instlist,
                                                     "tas": talist})
    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        accobj = UserClass.get_user(request.POST["account"])
        uname = request.POST["username"]
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]
        urole = request.POST["accrole"]
        contact = request.POST["contact"]

        try:
            if uname != accobj.username:
                UserClass.set_username(accobj,uname)
            UserClass.set_first_name(accobj,fname)
            UserClass.set_last_name(accobj,lname)
            UserClass.set_role(accobj,urole)
            UserClass.set_email(accobj,contact)
        except Exception as e:
            return render(request, "editTargetAccount.html", {"message": str(e),
                                                       "role": UserClass.get_role(my_user),
                                                       "account": accobj})
        return render(request, "viewTargetAccount.html", {"role": UserClass.get_role(my_user),
                                                          "account": accobj})


class editSelfAccount(View):
    def get(self, request):
        talist = UserClass.get_all_tas()
        instlist = UserClass.get_all_instructors()
        suplist = UserClass.get_all_supervisors()
        my_user = UserClass.get_user(request.session["session_username"])
        return render(request, "editSelfAccount.html", {"role": UserClass.get_role(my_user),
                                                     "all_users": UserClass.get_all_users(),
                                                     "supervisors": suplist,
                                                     "instructors": instlist,
                                                     "tas": talist})
    def post(self, request):
        my_user = UserClass.get_user(request.session["session_username"])
        accobj = UserClass.get_user(request.POST["account"])
        contact = request.POST["contact"]

        try:
            UserClass.set_email(accobj,contact)
        except Exception as e:
            return render(request, "editSelfAccount.html", {"message": str(e),
                                                              "role": UserClass.get_role(my_user),
                                                              "account": accobj})
        return render(request, "MyAccount.html", {"username": accobj.username,
                                                  "full_name": accobj.first_name + " " + accobj.last_name,
                                                  "role": accobj.role,
                                                  "email": accobj.email,
                                                  "courses": UserClass.get_courses(accobj),
                                                  "sections": UserClass.get_sections(accobj)})
