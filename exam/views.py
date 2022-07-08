from django.shortcuts import render
from urllib import response
from django.forms import FileField
from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404, HttpResponseRedirect
from exam.models import Course_exam
from .models import *
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse
from exam.forms import *
from django.http import HttpResponse
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from .models import Question,Result
from .models import models as SMODEL
from .forms import CourseForm
import os
from django.http  import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def teacher_dashboard_view(request):
    dict={
    
    'total_course':Course_exam.objects.all().count(),
    'total_question':Question.objects.all().count(),
    'total_student':Student.objects.all().count(),
    'total_dept':Dept.objects.all().count(),
    'total_subject':Course.objects.all().count()
    
}
    return render(request,'online/teacher_dashboard.html',context=dict)
def student_view(request):
    student=Student.objects.all()
    return render(request,'online/student_view.html',{'student':student})
def teacher_view(request):
    teacher=Teacher.objects.all()
    return render(request,'online/teacherview.html',{'student':teacher})
def teacher_exam_view(request):
    return render(request,'online/teacher_exam.html')

def teacher_add_exam_view(request):
    courseForm=CourseForm()
    if request.method=='POST':
        courseForm=CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('teacher-view-exam')
    return render(request,'online/teacher_add_exam.html',{'courseForm':courseForm})

def teacher_view_exam_view(request):
    courses =Course_exam.objects.all()
    return render(request,'online/teacher_view_exam.html',{'courses':courses})

def delete_exam_view(request,pk):
    course=Course_exam.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('teacher-view-exam')
def teacher_question_view(request):
    return render(request,'online/teacher_question.html')
def teacher_add_question_view(request):
    questionForm=QuestionForm()
    if request.method=='POST':
        questionForm=QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=Course_exam.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('teacher-view-question')
    return render(request,'online/teacher_add_question.html',{'questionForm':questionForm})

def teacher_view_question_view(request):
    courses=Course_exam.objects.all()
    return render(request,'online/teacher_view_question.html',{'courses':courses})

def see_question_view(request,pk):
    questions=Question.objects.all().filter(course_id=pk)
    return render(request,'online/see_question.html',{'questions':questions})
def remove_question_view(request,pk):
    question=Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('teacher-view-question')
#======================================================
#===================================================================
#==========================================================================

def student_dashboard_view(request):
    dict={
    
    'total_course':Course_exam.objects.all().count(),
    'total_question':Question.objects.all().count(),
    }
    return render(request,'student/student_dashboard.html',context=dict)
def student_exam_view(request):
    courses=Course_exam.objects.all()
    return render(request,'student/student_exam.html',{'courses':courses})
def take_exam_view(request,pk):
    course=Course_exam.objects.get(id=pk)
    total_questions=Question.objects.all().filter(course=course).count()
    questions=Question.objects.all().filter(course=course)
    total_marks=0
    for q in questions:
        total_marks=total_marks + q.marks
    
    return render(request,'student/take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks})
def start_exam_view(request,pk):
    course=Course_exam.objects.get(id=pk)
    questions=Question.objects.all().filter(course=course)
    if request.method=='POST':
        pass
    response= render(request,'student/start_exam.html',{'course':course,'questions':questions})
    response.set_cookie('course_id',course.id)
    return response
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course=Course_exam.objects.get(id=course_id)
        
        total_marks=0
        questions=Question.objects.all().filter(course=course)
        for i in range(len(questions)):
            
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = models.Student.objects.get(user_id=request.user.id)
        result =Result()
        result.marks=total_marks
        result.exam=course
        result.student=student
        result.save()

        return HttpResponseRedirect('view-result')


def view_result_view(request):
    courses=Course_exam.objects.all()
    return render(request,'student/view_result.html',{'courses':courses})
def check_marks_view(request,pk):
    course=Course_exam.objects.get(id=pk)
    results=Result.objects.all().filter(exam=course)
    return render(request,'student/check_marks.html',{'results':results})
def student_marks_view(request):
    courses=Course_exam.objects.all()
    return render(request,'student/student_marks.html',{'courses':courses})

# ========================================================
# ==========================================================
# =============================================
# ======================================================================
# ===================================

def home_view(request):
    return render(request,'quiz/index.html')

def admin_dashboard_view(request):
    dict={
    'total_student':Student.objects.all().count(),
    'total_teacher':Teacher.objects.all().count(),
    'total_Hod':hod_admin.objects.all().count(),
    'total_dept':Dept.objects.all().count(),
    'total_course':Course.objects.all().count(),
    }
    return render(request,'quiz/admin_dashboard.html',context=dict)
def admin_teacher_view(request):
    dict={
    'total_teacher':Teacher.objects.all().count(),
    'pending_teacher':Teacher_exam.objects.all().count(),
    }
    return render(request,'quiz/admin_teacher.html',context=dict)

def admin_view_teacher_view(request):
    teachers= Teacher.objects.all()
    return render(request,'quiz/admin_view_teacher.html',{'teachers':teachers})
def update_teacher_view(request,pk):
    teacher=hod_admin.objects.get(id=pk)
    user=hod_admin.objects.get(id=teacher.id)
    userForm=TeacherUserForm(instance=user)
    teacherForm=TeacherForm(request.FILES,instance=teacher)
    mydict={'userForm':userForm,'teacherForm':teacherForm}
    if request.method=='POST':
        userForm=TeacherUserForm(request.POST,instance=user)
        teacherForm=TeacherForm(request.POST,request.FILES,instance=teacher)
        if userForm.is_valid() and teacherForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            teacherForm.save()
            return redirect('admin-view-teacher')
    return render(request,'quiz/update_teacher.html',context=mydict)

def delete_teacher_view(request,pk):
    teacher=hod_admin.objects.get(id=pk)
    user=hod_admin.objects.get(id=teacher.id)
    user.delete()
    teacher.delete()
    return HttpResponseRedirect('/admin-view-teacher')
def admin_view_pending_teacher_view(request):
    teachers= hod_admin.objects.all()
    return render(request,'quiz/admin_view_pending_teacher.html',{'teachers':teachers})
def approve_teacher_view(request,pk):
    teacherSalary=TeacherSalaryForm()
    if request.method=='POST':
        teacherSalary=TeacherSalaryForm(request.POST)
        if teacherSalary.is_valid():
            teacher=hod_admin.objects.get(id=pk)
            teacher.salary=teacherSalary.cleaned_data['salary']
            teacher.status=True
            teacher.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-pending-teacher')
    return render(request,'quiz/salary_form.html',{'teacherSalary':teacherSalary})

def reject_teacher_view(request,pk):
    teacher=hod_admin.objects.get(id=pk)
    user=User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return HttpResponseRedirect('/admin-view-pending-teacher')

def admin_view_teacher_salary_view(request):
    teachers=hod_admin.objects.all().filter(status=True)
    return render(request,'quiz/admin_view_teacher_salary.html',{'teachers':teachers})

def admin_student_view(request):
    dict={
    'total_student':Student.objects.all().count(),
    }
    return render(request,'quiz/admin_student.html',context=dict)


def admin_view_student_view(request):
    students= Student.objects.all()
    return render(request,'quiz/admin_view_student.html',{'students':students})
def update_student_view(request,pk):
    student=Student_exam.objects.get(id=pk)
    user=Student_exam.objects.get(id=student.id)
    userForm=StudentUserForm(instance=user)
    studentForm=StudentForm(request.FILES,instance=student)
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=StudentUserForm(request.POST,instance=user)
        studentForm=StudentForm(request.POST,request.FILES,instance=student)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            studentForm.save()
            return redirect('admin-view-student')
    return render(request,'quiz/update_student.html',context=mydict)
def delete_student_view(request,pk):
    student=Student_exam.objects.get(id=pk)
    user=Student_exam.objects.get(id=student.id)
    user.delete()
    student.delete()
    return HttpResponseRedirect('/admin-view-student')
def admin_course_view(request):
    return render(request,'quiz/admin_course.html')
def admin_add_course_view(request):
    courseForm=CourseForm()
    if request.method=='POST':
        courseForm=CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-course')
    return render(request,'quiz/admin_add_course.html',{'courseForm':courseForm})
def admin_view_course_view(request):
    courses =Course_exam.objects.all()
    return render(request,'quiz/admin_view_course.html',{'courses':courses})
def delete_course_view(request,pk):
    course=Course_exam.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/admin-view-course')

def admin_question_view(request):
    return render(request,'quiz/admin_question.html')

def admin_add_question_view(request):
    questionForm=QuestionForm()
    if request.method=='POST':
        questionForm=QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=Course_exam.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-question')
    return render(request,'quiz/admin_add_question.html',{'questionForm':questionForm})

def admin_view_question_view(request):
    courses=Course_exam.objects.all()
    return render(request,'quiz/admin_view_question.html',{'courses':courses})
def view_question_view(request,pk):
    questions=Question.objects.all().filter(course_id=pk)
    return render(request,'quiz/view_question.html',{'questions':questions})
def delete_question_view(request,pk):
    question=Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/admin-view-question')
def admin_view_student_marks_view(request):
    students=Student_exam.objects.all()
    return render(request,'quiz/admin_view_student_marks.html',{'students':students})
def admin_view_marks_view(request,pk):
    courses =Course_exam.objects.all()
    response =  render(request,'quiz/admin_view_marks.html',{'courses':courses})
    response.set_cookie('student_id',str(pk))
    return response
def admin_check_marks_view(request,pk):
    course =Course_exam.objects.get(id=pk)
    student_id = request.COOKIES.get('student_id')
    student=Student_exam.objects.get(id=student_id)

    results=Result.objects.all().filter(exam=course)
    return render(request,'quiz/admin_check_marks.html',{'results':results})
    




def aboutus_view(request):
    return render(request,'quiz/aboutus.html')

def contactus_view(request):
    sub = ContactusForm()
    if request.method == 'POST':
        sub = ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'quiz/contactussuccess.html')
    return render(request, 'quiz/contactus.html', {'form':sub})