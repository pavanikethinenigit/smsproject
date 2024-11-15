from django import forms
from .models import Task
from .models import StudentList


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=['title']

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']
# Register_Number = forms.CharField(max_length=10, min_length=10, label="Student ID",
    #                              error_messages={
    #                                  'required': 'Student ID is required',
    #                                  'min_length': 'Student ID must be exactly 10 characters',
    #                                  'max_length': 'Student ID must be exactly 10 characters'
    #                              })
    # Name = forms.CharField(max_length=100, label="Student Name",
    #                                error_messages={'required': 'Student name is required'})


class UploadFileForm(forms.Form):
    file = forms.FileField()

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'experience', 'usability', 'features', 'comments', 'recommend']

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address']







