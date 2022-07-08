from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Admin, Event, Book_ground

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Event)
admin.site.register(Book_ground)
