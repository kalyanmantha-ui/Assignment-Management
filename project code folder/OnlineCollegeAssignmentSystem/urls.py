"""OnlineCollegeAssignmentSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from collegeAssignment.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

#================ Admin URL ===============================

    path('admin_login', admin_login, name='admin_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('course', course, name='course'),
    path('editCourse/<int:pid>', editCourse, name='editCourse'),
    path('deleteCourse/<int:pid>', deleteCourse, name='deleteCourse'),
    path('subject', subject, name='subject'),
    path('editSubject/<int:pid>', editSubject, name='editSubject'),
    path('deleteSubject/<int:pid>', deleteSubject, name='deleteSubject'),
    path('teacher', teacher, name='teacher'),
    path('editTeacher/<int:pid>', editTeacher, name='editTeacher'),
    path('deleteTeacher/<int:pid>', deleteTeacher, name='deleteTeacher'),
    path('regUser', regUser, name='regUser'),
    path('deleteUser/<int:pid>', deleteUser, name='deleteUser'),
    path('news', news, name='news'),
    path('editNews/<int:pid>', editNews, name='editNews'),
    path('deleteNews/<int:pid>', deleteNews, name='deleteNews'),
    path('btwdateAssign', btwdateAssign, name='btwdateAssign'),
    path('adminviewsubmitAssign/<int:pid>', adminviewsubmitAssign, name='adminviewsubmitAssign'),
    path('search', search, name='search'),
    path('unchecked_Assignment', unchecked_Assignment, name='unchecked_Assignment'),
    path('checked_Assignment', checked_Assignment, name='checked_Assignment'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout/', Logout, name='logout'),

# ================ Teacher URL ===============================

    path('teacher_login', teacher_login, name='teacher_login'),
    path('teacherProfile', teacherProfile, name='teacherProfile'),
    path('tdashboard', tdashboard, name='tdashboard'),
    path('teacherAssignment', teacherAssignment, name='teacherAssignment'),
    path('editAssignment/<int:pid>', editAssignment, name='editAssignment'),
    path('load_subject/', load_subject, name="ajax_load_subject"),
    path('teacherNews', teacherNews, name='teacherNews'),
    path('editTeacherNews/<int:pid>', editTeacherNews, name='editTeacherNews'),
    path('deleteTeacherNews/<int:pid>', deleteTeacherNews, name='deleteTeacherNews'),
    path('unchecked_Assign', unchecked_Assign, name='unchecked_Assign'),
    path('viewUncheckedAssign/<int:pid>', viewUncheckedAssign, name='viewUncheckedAssign'),
    path('checked_Assign', checked_Assign, name='checked_Assign'),
    path('viewCheckedAssign/<int:pid>', viewCheckedAssign, name='viewCheckedAssign'),
    path('subjectwiseReport', subjectwiseReport, name='subjectwiseReport'),
    path('teacherviewsubmitAssign/<int:pid>', teacherviewsubmitAssign, name='teacherviewsubmitAssign'),
    path('regCoursewiseUser', regCoursewiseUser, name='regCoursewiseUser'),
    path('teacherchangePassword', teacherchangePassword, name='teacherchangePassword'),



# ================ Student URL ===============================
    path('student_login', student_login, name='student_login'),
    path('studentProfile', studentProfile, name='studentProfile'),
    path('signup', signup, name='signup'),
    path('sdashboard', sdashboard, name='sdashboard'),
    path('newAssignment', newAssignment, name='newAssignment'),
    path('submitAssignment/<int:pid>', submitAssignment, name='submitAssignment'),
    path('viewsubmitAssign/<int:pid>', viewsubmitAssign, name='viewsubmitAssign'),
    path('uploadAssignment', uploadAssignment, name='uploadAssignment'),
    path('studentchangePassword', studentchangePassword, name='studentchangePassword'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
