from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from onlinelibrary import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from this import s
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from exam import views
from onlinelibrary import views as v1
from sport_event import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='info/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='info/logout.html'), name='logout'),
        #===========================library_tempalates==========================

    path("library",v1.library),
    path("librarylogin",v1.librarylogin),
    path("manage_student",v1.manage_students),
    path("managestudent",v1.managestudent),
    path("viewstudent",v1.viewstudent),
    path("student_view1",v1.student_view1),
    path("teacher_add",v1.teacher_add),
    path("teacher_view1",v1.teacher_view1),
    path("book_add",v1.book_add),
    path("book_view",v1.book_view),
    path("bookfine",v1.bookfine),
    path('issuebook', v1.issuebook, name='issue'),
    path('retrive_blog', v1.retrive_blog, name='retrieve-blog'),
    path('update/<int:pk>', v1.update_blog, name='update-blog'),
    path('delete/<int:pk>', v1.delete_blog, name='delete-blog'),
    path('delete_student/<int:pk>',v1.delete_student,name='delete-student'),
    path('library_books_download', v1.library_books_download, name='library_books_download'),
    path('view_student/<int:pk>',v1.view_student,name='view-student-pk'),
    path('borrows',v1.borrows,name='borrow-page'),
    path('manage_borrow',v1.manage_borrow,name='manage-borrow'),
    path('manage_borrow/<int:pk>',v1.manage_borrow,name='manage-borrow-pk'),
    path('delete_borrow/<int:pk>',v1.delete_borrow,name='delete-borrow'),
    path('save_borrow/<int:pk>',v1.save_borrow,name='save-borrow'),
    path('save_borrow',v1.save_borrow,name='save-borrow'),

    path('view_borrow/<int:pk>',v1.view_borrow,name='view-borrow-pk'),
    path('books',v1.books,name='book-page'),
    path('manage_book',v1.manage_book,name='manage-book'),
    path('manage_book/<int:pk>',v1.manage_book,name='manage-book-pk'),
    path('view_book/<int:pk>',v1.view_book,name='view-book-pk'),
    path('save_book',v1.save_book,name='save-book'),
    path('delete_book/<int:pk>',v1.delete_book,name='delete-book'),

    #========================================exam-====================

path('aboutus', views.aboutus_view),
path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
path('admin-teacher', views.admin_teacher_view,name='admin-teacher'),
path('admin-view-teacher', views.admin_view_teacher_view,name='admin-view-teacher'),
path('update-teacher/<int:pk>', views.update_teacher_view,name='update-teacher'),
path('delete-teacher/<int:pk>', views.delete_teacher_view,name='delete-teacher'),
path('admin-view-pending-teacher', views.admin_view_pending_teacher_view,name='admin-view-pending-teacher'),
path('admin-view-teacher-salary', views.admin_view_teacher_salary_view,name='admin-view-teacher-salary'),
path('approve-teacher/<int:pk>', views.approve_teacher_view,name='approve-teacher'),
path('reject-teacher/<int:pk>', views.reject_teacher_view,name='reject-teacher'),
path('admin-student', views.admin_student_view,name='admin-student'),
path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
path('admin-view-student-marks', views.admin_view_student_marks_view,name='admin-view-student-marks'),
path('admin-view-marks/<int:pk>', views.admin_view_marks_view,name='admin-view-marks'),
path('admin-check-marks/<int:pk>', views.admin_check_marks_view,name='admin-check-marks'),
path('update-student/<int:pk>', views.update_student_view,name='update-student'),
path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
path('admin-course', views.admin_course_view,name='admin-course'),
path('admin-add-course', views.admin_add_course_view,name='admin-add-course'),
path('admin-view-course', views.admin_view_course_view,name='admin-view-course'),
path('delete-course/<int:pk>', views.delete_course_view,name='delete-course'),
path('admin-question', views.admin_question_view,name='admin-question'),
path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
path('admin-view-question', views.admin_view_question_view,name='admin-view-question'),
path('view-question/<int:pk>', views.view_question_view,name='view-question'),
path('delete-question/<int:pk>', views.delete_question_view,name='delete-question'),
path('teacher_dashboard_view', views.teacher_dashboard_view,name='teacher-dashboard'),
path('student_view',views.student_view),
#========================================================
path('teacher_view',views.teacher_view),
path('teacher_exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher_add_exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('online/teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete_exam/<int:pk>', views.delete_exam_view,name='delete-exam'),
path('teacher_question', views.teacher_question_view,name='teacher-question'),
path('teacher_add_question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher_view_question', views.teacher_view_question_view,name='teacher-view-question'),
path('see_question/<int:pk>', views.see_question_view,name='see-question'),
path('remove_question/<int:pk>', views.remove_question_view,name='remove-question'),

 #================================online exam STUDENT  =======================
path('student_dashboard', views.student_dashboard_view,name='student-dashboard'),
path('student_exam', views.student_exam_view,name='student-exam'),
path('take_exam/<int:pk>', views.take_exam_view,name='take-exam'),
path('start_exam/<int:pk>', views.start_exam_view,name='start-exam'),
path('calculate_marks', views.calculate_marks_view,name='calculate-marks'),
path('view_result', views.view_result_view,name='view-result'),
path('check_marks/<int:pk>', views.check_marks_view,name='check-marks'),
path('student_marks', views.student_marks_view,name='student-marks'),







#====================================sport event-------------------------------------
    path('registration',v2.index),
    path('user_home',v2.user_home),
    path('test',v2.test,name='test'),
    path('login_user',v2.login_user,name='login_user'),

    path('admin_login',v2.admin_login,name='admin_login'),
    path('login_admin',v2.login_admin,name='login_admin'),

    path('admin_home',v2.admin_home,name='admin_home'),
    path('user_home',v2.user_home,name='user_home'),

    path('user_event',v2.user_event,name='user_event'),
    path('ground_booking',v2.ground_booking,name='ground_booking'),
    path('db_ground_booking',v2.db_ground_booking,name='db_ground_booking'),

    path('admin_booking',v2.admin_booking,name='admin_booking'),
    path('admin_event',v2.admin_event,name='admin_event'),

    path('update_event/(?P<id>\d+)/$',v2.update_event,name='update_event'),
    path('db_update_event/(id)',v2.db_update_event,name='db_update_event'),
    path('db_delete_event/(?P<id>\d+)',v2.db_delete_event,name='db_delete_event'),

    path('add_event',v2.add_event,name='add_event'),
    path('db_add_event',v2.db_add_event,name='db_add_event'),

    path('user_logout',v2.user_logout,name='user_logout'),
    path('admin_logout',v2.admin_logout,name='admin_logout'),





    path('borrow',v1.borrow),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,)