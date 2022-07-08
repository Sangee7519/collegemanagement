from django import forms
from django.forms import ModelForm
from .models import *

class student_views_form(forms.ModelForm):  
    class Meta:  
        model =student_views
        fields = "__all__"  
class book_issue_form(forms.ModelForm):
    class Meta:
        model=book_issue
        fields="__all__" 