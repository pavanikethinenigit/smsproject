from django.shortcuts import render, redirect, get_object_or_404
from adminapp.forms import TaskForm
from adminapp.models import Task


# Create your views here.
def FacultyHomePage(request):
    return render(request, 'facultyapp/FacultyHomePage.html')


'''
def add_task(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form=TaskForm()
        tasks=Task.objects.all()
        return render(request, 'faculty/add_task.html', {'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')
'''

from .forms import AddCourseForm, Task_Form, MarksForm


def add_course(request):
    if request.method=='POST':
        form=AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:FacultyHomePage')
    else:
        form=AddCourseForm()
    return render(request, 'facultyapp/add_course.html', {'form':form})

# def view_student_list(request):
#     students = StudentList.objects.all()
#     return render(request, 'facultyapp/students.html')

def add_blog(request):
    if request.method == "POST":
        form = Task_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:add_blog')
    else:
        form = Task_Form()
    tasks = Task.objects.all()
    return render(request, 'facultyapp/BlogSiteManager.html', {'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('facultyapp:add_blog')

from .forms import AddCourseForm
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:FacultyHomePage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/AddCourse.html', {'form': form})


from .models import AddCourse
from adminapp.models import StudentList

def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/students.html', context)

from django.core.mail import send_mail
from django.contrib.auth.models import User  # Assuming User is your custom user model
from .models import StudentList


def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the student in the form
            student = marks_instance.student
            student_user = student.User
            user_email = student_user.email

            subject = 'Marks Entered'
            message = f'Hello, {student_user.first_name}  marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
            from_email = 'neha.avanigadda@gmail.com'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'facultyapp/marks_success.html')
    else:
        form = MarksForm()
    return render(request, 'facultyapp/post_marks.html', {'form': form})

