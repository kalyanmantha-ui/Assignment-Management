from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Course(models.Model):
    BranchName = models.CharField(max_length=150, null=True)
    CourseName = models.CharField(max_length=200, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.CourseName


class Teacher(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    EmpID = models.IntegerField(null=True)
    MobileNumber = models.CharField(max_length=15, null=True)
    Gender = models.CharField(max_length=50, null=True)
    Dob = models.DateField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Religion = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=300, null=True)
    ProfilePic = models.FileField(max_length=200, null=True)
    JoiningDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.users.first_name


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    SubjectFullname = models.CharField(max_length=200, null=True)
    SubjectShortname = models.CharField(max_length=50, null=True)
    SubjectCode = models.CharField(max_length=50, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.SubjectFullname


class Assigment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    AssignmentNumber = models.IntegerField(null=True)
    AssignmentTitle = models.CharField(max_length=150, null=True)
    AssignmentDescription = models.CharField(max_length=300, null=True)
    SubmissionDate = models.DateField(null=True)
    AssignmentMarks = models.CharField(max_length=150, null=True)
    AssignmentFile = models.FileField(max_length=200, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.CourseName


class News(models.Model):
    Title = models.CharField(max_length=200, null=True)
    Description = models.CharField(max_length=500, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title


class Newsbyteacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200, null=True)
    Description = models.CharField(max_length=500, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    MobileNumber = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    RollNumber = models.CharField(max_length=200, null=True)
    RegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class Uploadass(models.Model):
    assignment = models.ForeignKey(Assigment, on_delete=models.CASCADE)
    userdetail = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    Assdesc = models.CharField(max_length=300, null=True)
    AnswerFile = models.FileField(null=True)
    SubmitDate = models.DateField(null=True)
    Marks = models.CharField(max_length=100, null=True)
    Remarks = models.CharField(max_length=250, null=True)
    UpdationDate = models.DateField(null=True)

    def __str__(self):
        return self.Assdesc

