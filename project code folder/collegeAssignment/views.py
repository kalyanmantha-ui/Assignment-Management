from datetime import date

from django.db.models import Max, Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login


# Create your views here.

# =================  Admin View ===========================

def index(request):
    news = News.objects.all()
    return render(request, 'index.html', locals())


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalcourse = Course.objects.all().count()
    totalsubject = Subject.objects.all().count()
    totalteacher = Teacher.objects.all().count()
    totaluser = UserDetail.objects.all().count()
    return render(request, 'dashboard.html', locals())


def course(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    course = Course.objects.all()
    try:
        if request.method == "POST":
            courseName = request.POST['CourseName']
            branchName = request.POST['BranchName']

            try:
                Course.objects.create(CourseName=courseName, BranchName=branchName)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'course.html', locals())


def editCourse(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    course = Course.objects.get(id=pid)
    if request.method == "POST":
        courseName = request.POST['CourseName']
        branchName = request.POST['BranchName']

        course.CourseName = courseName
        course.BranchName = branchName

        try:
            course.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editCourse.html', locals())


def deleteCourse(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    course = Course.objects.get(id=pid)
    course.delete()
    return redirect('course.html')


def subject(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    course = Course.objects.all()
    subject = Subject.objects.all()
    try:
        if request.method == "POST":
            courid = request.POST['course']
            courseid = Course.objects.get(id=courid)

            subfullName = request.POST['SubjectFullname']
            subShortName = request.POST['SubjectShortname']
            subcode = request.POST['SubjectCode']

            try:
                Subject.objects.create(course=courseid, SubjectFullname=subfullName, SubjectShortname=subShortName,
                                       SubjectCode=subcode)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'subject.html', locals())


def editSubject(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    course = Course.objects.all()
    subject = Subject.objects.get(id=pid)
    if request.method == "POST":
        cid = request.POST['course']
        courseid = Course.objects.get(id=cid)

        subfullName = request.POST['SubjectFullname']
        subShortName = request.POST['SubjectShortname']
        subcode = request.POST['SubjectCode']

        subject.course = courseid
        subject.SubjectFullname = subfullName
        subject.SubjectShortname = subShortName
        subject.SubjectCode = subcode

        try:
            subject.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editSubject.html', locals())


def deleteSubject(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    subject = Subject.objects.get(id=pid)
    subject.delete()
    return redirect('subject.html')


def teacher(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    course = Course.objects.all()
    teacher = Teacher.objects.all()
    try:
        empid = 1001 if Teacher.objects.count() == 0 else Teacher.objects.aggregate(max=Max('EmpID'))["max"] + 1
        error = ""
        if request.method == "POST":

            coreid = request.POST['course']
            coursesid = Course.objects.get(id=coreid)

            fname = request.POST['firstName']
            lname = request.POST['lastName']
            mob = request.POST['MobileNumber']
            e = request.POST['email']
            pwd = request.POST['password']
            gender = request.POST['Gender']
            dob = request.POST['Dob']
            religion = request.POST['Religion']
            address = request.POST['Address']
            profilepic = request.FILES['ProfilePic']

            try:
                user = User.objects.create_user(username=e, password=pwd, first_name=fname, last_name=lname)
                Teacher.objects.create(users=user, course=coursesid, EmpID=empid, MobileNumber=mob, Gender=gender,
                                       Dob=dob, Religion=religion, Address=address, ProfilePic=profilepic)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'teacher.html', locals())


def editTeacher(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    course = Course.objects.all()
    teacher = Teacher.objects.get(id=pid)
    if request.method == "POST":
        coreid = request.POST['course']
        courseid = Course.objects.get(id=coreid)

        fname = request.POST['firstName']
        lname = request.POST['lastName']
        mob = request.POST['MobileNumber']
        gender = request.POST['Gender']
        dob = request.POST['Dob']
        religion = request.POST['Religion']
        address = request.POST['Address']

        teacher.users.first_name = fname
        teacher.users.last_name = lname
        teacher.course = courseid
        teacher.MobileNumber = mob
        teacher.Gender = gender
        teacher.Dob = dob
        teacher.Religion = religion
        teacher.Address = address

        try:
            teacher.save()
            teacher.users.save()
            error = "no"
        except:
            error = "yes"

        try:
            profilePic = request.FILES['ProfilePic']
            teacher.ProfilePic = profilePic
            teacher.save()
        except:
            pass
    return render(request, 'editTeacher.html', locals())


def deleteTeacher(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    User.objects.get(id=pid).delete()
    return redirect('teacher.html')


def regUser(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userDtls = UserDetail.objects.all()
    return render(request, 'regUser.html', locals())


def deleteUser(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    User.objects.get(id=pid).delete()
    return redirect('regUser.html')


def news(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    news = News.objects.all()
    try:
        if request.method == "POST":
            title = request.POST['Title']
            description = request.POST['Description']

            try:
                News.objects.create(Title=title, Description=description)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'news.html', locals())


def editNews(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    news = News.objects.get(id=pid)
    if request.method == "POST":
        title = request.POST['Title']
        description = request.POST['Description']

        news.Title = title
        news.Description = description

        try:
            news.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editNews.html', locals())


def deleteNews(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    news = News.objects.get(id=pid)
    news.delete()
    return redirect('news.html')


def unchecked_Assignment(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    sd = None
    subject = Subject.objects.all()
    if request.method == 'POST':
        sd = request.POST['subject']
        teachersubject = Subject.objects.get(id=sd)
        assignment = Assigment.objects.filter(subject=teachersubject)
        uploadassignment = Uploadass.objects.filter(assignment__in=assignment, Remarks=None)
    return render(request, 'unchecked_Assignment.html', locals())


def checked_Assignment(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    sd = None
    subject = Subject.objects.all()
    if request.method == 'POST':
        sd = request.POST['subject']
        teachersubject = Subject.objects.get(id=sd)
        assignment = Assigment.objects.filter(subject=teachersubject)
        uploadassignment = Uploadass.objects.filter(assignment__in=assignment, Remarks__isnull=False)
    return render(request, 'checked_Assignment.html', locals())


def btwdateAssign(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['FromDate']
        td = request.POST['ToDate']

        uploadass = Uploadass.objects.filter(Q(SubmitDate__gte=fd) & Q(SubmitDate__lte=td))
        return render(request, 'bwdatesReportAssindetails.html', locals())
    return render(request, 'btwdateAssign.html')


def adminviewsubmitAssign(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    uploadAssign = Uploadass.objects.get(id=pid)
    return render(request, 'adminviewsubmitAssign.html', locals())


def search(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sd = None
    bankdtls = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
        user = [i.id for i in User.objects.filter(Q(first_name__icontains=sd) | Q(last_name__icontains=sd))]
        teacher = [i.id for i in Teacher.objects.filter(Q(users__in=user))]
        subject = [i.id for i in Subject.objects.filter(
            Q(SubjectFullname__icontains=sd) | Q(SubjectShortname=sd) | Q(SubjectCode=sd))]
        assignment = [i.id for i in Assigment.objects.filter(
            Q(teacher__in=teacher) | Q(subject__in=subject) | Q(AssignmentNumber__icontains=sd))]
        uploadass = Uploadass.objects.filter(Q(assignment__in=assignment))
    return render(request, 'search.html', locals())


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')


# ================= Teacher View ===========================

def teacher_login(request):
    error = ""
    if request.method == 'POST':
        email = request.POST['Email']
        pwd = request.POST['Password']
        user = authenticate(username=email, password=pwd)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'teacher_login.html', locals())


def tdashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = request.user
    teacher = Teacher.objects.get(users=user)
    teachercourse = teacher.course
    totalStudent = UserDetail.objects.filter(course=teachercourse).count()
    totalAssig = Assigment.objects.filter(teacher=teacher).count()
    totalAnnoucement = Newsbyteacher.objects.filter(teacher=teacher).count()
    return render(request, 'tdashboard.html', locals())


def teacherAssignment(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')

    course = Course.objects.all()
    subject = Subject.objects.all()

    user = User.objects.get(id=request.user.id)
    teacher = Teacher.objects.get(users=user)

    teachercourse = teacher.course
    assignment = Assigment.objects.filter(teacher=teacher)
    teachersub = Subject.objects.filter(course=teachercourse)
    try:
        assignmentNumber = 10001 if Assigment.objects.count() == 0 else \
            Assigment.objects.aggregate(max=Max('AssignmentNumber'))["max"] + 1
        error = ""
        if request.method == "POST":
            cid = request.POST['course']
            courseid = Course.objects.get(id=cid)

            sid = request.POST['subject']
            subjectid = Subject.objects.get(id=sid)

            assigTitle = request.POST['AssignmentTitle']
            assigDesc = request.POST['AssignmentDescription']
            subDate = request.POST['SubmissionDate']
            assigMarks = request.POST['AssignmentMarks']
            assigFile = request.FILES['AssignmentFile']

            try:
                Assigment.objects.create(course=courseid, subject=subjectid, teacher=teacher,
                                         AssignmentNumber=assignmentNumber, AssignmentTitle=assigTitle,
                                         AssignmentDescription=assigDesc, SubmissionDate=subDate,
                                         AssignmentMarks=assigMarks, AssignmentFile=assigFile)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'teacherAssignment.html', locals())


def editAssignment(request, pid):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    error = ""

    course = Course.objects.all()
    subject = Subject.objects.all()
    assignment = Assigment.objects.get(id=pid)

    if request.method == "POST":
        coreid = request.POST['course']
        courseid = Course.objects.get(id=coreid)

        subid = request.POST['subject']
        subjectid = Subject.objects.get(id=subid)

        assigntitle = request.POST['AssignmentTitle']
        assigndesc = request.POST['AssignmentDescription']
        subdate = request.POST['SubmissionDate']
        assignmarks = request.POST['AssignmentMarks']

        assignment.course = courseid
        assignment.subject = subjectid
        assignment.AssignmentTitle = assigntitle
        assignment.AssignmentDescription = assigndesc
        assignment.SubmissionDate = subdate
        assignment.AssignmentMarks = assignmarks

        try:
            assignment.save()
            error = "no"
        except:
            error = "yes"
        try:
            assignmentFile = request.FILES['AssignmentFile']
            assignment.AssignmentFile = assignmentFile
            assignment.save()
        except:
            pass
    return render(request, 'editAssignment.html', locals())


def teacherNews(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')

    user = User.objects.get(id=request.user.id)
    teacher = Teacher.objects.get(users=user)
    newsbyTeacher = Newsbyteacher.objects.filter(teacher=teacher)

    try:
        error = ""
        if request.method == "POST":
            title = request.POST['Title']
            description = request.POST['Description']

            try:
                Newsbyteacher.objects.create(teacher=teacher, Title=title, Description=description)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'teacherNews.html', locals())


def editTeacherNews(request, pid):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    error = ""
    teacher = Teacher.objects.all()
    newsteacher = Newsbyteacher.objects.get(id=pid)
    if request.method == "POST":
        title = request.POST['Title']
        description = request.POST['Description']

        newsteacher.Title = title
        newsteacher.Description = description

        try:
            newsteacher.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editTeacherNews.html', locals())


def deleteTeacherNews(request, pid):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    newsteacher = Newsbyteacher.objects.get(id=pid)
    newsteacher.delete()
    return redirect('teacherNews.html')


def unchecked_Assign(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')

    sd = None
    user = request.user
    teacher = Teacher.objects.get(users=user)

    course = [i.id for i in Course.objects.filter(teacher=teacher)]
    subject = Subject.objects.filter(course__in=course)

    if request.method == 'POST':
        sd = request.POST['subject']
        teachersubject = Subject.objects.get(id=sd)
        assignment = Assigment.objects.filter(subject=teachersubject)
        uploadassignment = Uploadass.objects.filter(assignment__in=assignment, Remarks=None)
    return render(request, 'unchecked_Assign.html', locals())


def viewUncheckedAssign(request, pid):
    if not request.user.is_authenticated:
        return redirect('teacher_login')

    error = ""
    uploadass = Uploadass.objects.get(id=pid)

    if request.method == 'POST':
        remarks = request.POST['Remarks']
        marks = request.POST['Marks']

        try:
            uploadass.Remarks = remarks
            uploadass.Marks = marks
            uploadass.UpdationDate = date.today()

            uploadass.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'viewUncheckedAssign.html', locals())


def checked_Assign(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    sd = None

    user = request.user
    teacher = Teacher.objects.get(users=user)

    course = [i.id for i in Course.objects.filter(teacher=teacher)]
    subject = Subject.objects.filter(course__in=course)

    if request.method == 'POST':
        sd = request.POST['subject']
        teachersubject = Subject.objects.get(id=sd)
        assignment = Assigment.objects.filter(subject=teachersubject)
        uploadassignment = Uploadass.objects.filter(assignment__in=assignment, Remarks__isnull=False)
    return render(request, 'checked_Assign.html', locals())


def viewCheckedAssign(request, pid):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    uploadass = Uploadass.objects.get(id=pid)
    return render(request, 'viewCheckedAssign.html', locals())


def subjectwiseReport(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')

    user = request.user
    teacher = Teacher.objects.get(users=user)

    course = [i.id for i in Course.objects.filter(teacher=teacher)]
    subject = Subject.objects.filter(course__in=course)

    if request.method == "POST":
        fd = request.POST['FromDate']
        td = request.POST['ToDate']
        sd = request.POST['subject']
        teachersubject = Subject.objects.get(id=sd)
        assignment = Assigment.objects.filter(subject=teachersubject)

        uploadass = Uploadass.objects.filter(Q(SubmitDate__gte=fd) & Q(SubmitDate__lte=td) & Q(assignment__in=assignment))
        return render(request, 'bwdatesubjectwiseReport.html', locals())
    return render(request, 'subjectwiseReport.html',locals())


def teacherviewsubmitAssign(request, pid):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    uploadAssign = Uploadass.objects.get(id=pid)
    return render(request, 'teacherviewsubmitAssign.html', locals())


def regCoursewiseUser(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    user = request.user
    teachercourse = Teacher.objects.get(users=user).course
    print(teachercourse)
    userDtls = UserDetail.objects.filter(course=teachercourse)
    return render(request, 'regCoursewiseUser.html', locals())


def teacherProfile(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    user = User.objects.get(id=request.user.id)
    teacher = Teacher.objects.get(users=user)
    return render(request, 'teacherProfile.html', locals())


def teacherchangePassword(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'teacherchangePassword.html', locals())


def load_subject(request):
    courseid = request.GET.get('course')
    # course = Course.objects.get(id=courseid)
    subject = Subject.objects.filter(course=courseid)
    return render(request, 'subject_dropdown_list_options.html', locals())


# ================= Student View ===========================

def signup(request):
    error = ""
    course = Course.objects.all()
    if request.method == "POST":
        coreid = request.POST['course']
        courseid = Course.objects.get(id=coreid)

        fname = request.POST['firstName']
        lname = request.POST['lastName']
        email = request.POST['emailId']
        pwd = request.POST['Password']
        mob = request.POST['MobileNumber']
        rollno = request.POST['RollNumber']

        try:
            user = User.objects.create_user(username=email, password=pwd, first_name=fname, last_name=lname)
            UserDetail.objects.create(user=user, course=courseid, MobileNumber=mob, RollNumber=rollno)
            error = "no"
        except:
            error = "yes"
    return render(request, 'signup.html', locals())


def student_login(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['email']
        pwd = request.POST['password']
        user = authenticate(username=e, password=pwd)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'student_login.html', locals())


def sdashboard(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    user = request.user
    Usercourse = UserDetail.objects.get(user = user).course
    teacher = Teacher.objects.filter(course = Usercourse)
    teacherNews = Newsbyteacher.objects.filter(teacher__in = teacher)
    return render(request, 'sdashboard.html', locals())


def newAssignment(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    user = request.user
    StudentUser = UserDetail.objects.get(user=user)
    Usercourse = StudentUser.course
    teacher = Teacher.objects.filter(course=Usercourse)

    assignment = Assigment.objects.filter(teacher__in = teacher)
    uploadassignment = Uploadass.objects.filter(userdetail=StudentUser)

    li = []
    for i in uploadassignment:
        li.append(i.assignment.id)
    return render(request, 'newAssignment.html', locals())


def submitAssignment(request, pid):
    if not request.user.is_authenticated:
        return redirect('student_login')

    assignment = Assigment.objects.get(id=pid)

    user = User.objects.get(id=request.user.id)
    userDetails = UserDetail.objects.get(user=user)

    try:
        error = ""
        if request.method == "POST":
            assdesc = request.POST['Assdesc']
            ansfile = request.FILES['AnswerFile']

            try:
                Uploadass.objects.create(assignment=assignment, userdetail=userDetails, Assdesc=assdesc,
                                         AnswerFile=ansfile, SubmitDate=date.today())
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'submitAssignment.html', locals())


def uploadAssignment(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    uploadAssign = Uploadass.objects.filter(SubmitDate__isnull=False)
    return render(request, 'uploadAssignment.html', locals())


def viewsubmitAssign(request, pid):
    if not request.user.is_authenticated:
        return redirect('student_login')
    uploadAssign = Uploadass.objects.get(id=pid)
    return render(request, 'viewsubmitAssign.html', locals())


def studentchangePassword(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'studentchangePassword.html', locals())


def studentProfile(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    user = User.objects.get(id=request.user.id)
    userDtls = UserDetail.objects.get(user=user)

    if request.method == "POST":

        fname = request.POST['firstName']
        lname = request.POST['lastName']
        mob = request.POST['MobileNumber']

        userDtls.user.first_name = fname
        userDtls.user.last_name = lname
        userDtls.MobileNumber = mob

        try:
            userDtls.save()
            userDtls.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'studentProfile.html', locals())
