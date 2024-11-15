from django import forms
from .models import AddCourse,Task,Marks

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']


class Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content']

class MarksForm (forms.ModelForm):
    class Meta:
        model= Marks
        fields = ['student', 'course', 'marks']

