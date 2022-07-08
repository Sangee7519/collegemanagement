from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Course_exam)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Teacher_exam)
admin.site.register(Student_exam)