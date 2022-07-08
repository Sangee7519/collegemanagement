from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(teacher_views)
admin.site.register(manage_student)
admin.site.register(student_views)
admin.site.register(bookCSE)
admin.site.register(bookEEE)
admin.site.register(bookECE)
admin.site.register(bookCIVIL)
admin.site.register(bookMECh)
admin.site.register(entertaiment)
admin.site.register(comices)
admin.site.register(biography)
admin.site.register(history)
admin.site.register(novel)
admin.site.register(sci_fic)
admin.site.register(book_issue)
admin.site.register(fileAdmin)
admin.site.register(fine)
admin.site.register(Books)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(transactions)
admin.site.register(Borrow)