import matplotlib
from django.http import HttpResponse
from django.shortcuts import render
def projecthomepage(request):
    return render(request,'adminapp/ProjectHomepage.html')

def pagedividecall(request):
    return render(request, 'adminapp/pagediv.html')

# Create your views here.
def printpagecall(request):
    return render(request,'adminapp/printer.html')

def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input:{user_input}')
    a1= {'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)

def excepttionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num =int(user_input)
            result = 10/num
        except Exception as e:
            error_message =  str(e)
        return render(request, 'adminapp/ExceptionExample.html',{'result': result,'error':error_message})
    return render(request, 'adminapp/ExceptionExample.html')

import random
import string


def randompagecall(request):
    return render(request, 'adminapp/randomexample.html')


def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran': ran}
    return render(request, 'adminapp/randomexample.html', a1)

def calculatorpagecall(request):
    return render(request, 'adminapp/calculator.html')

def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def add_task(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form=TaskForm()
        tasks=Task.objects.all()
        return render(request, 'adminapp/add_task.html', {'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.urls import reverse



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            # Create the user and redirect to the homepage
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('ProjectHomepage')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'adminapp/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    else:
        return render(request, 'adminapp/login.html')

def log_out(request):
    auth.logout(request)
    return redirect('ProjectHomepage')


from django.utils import timezone
import datetime
import time
import pytz


# Import this at the top with other imports


def calculate_future_date(request):
    future_date = None
    if request.method == "POST":
        days_input = int(request.POST.get('days_input'))
        # Add the number of days to the current date
        current_time = timezone.now()  # Use timezone.now() to get the current time
        future_date = current_time + datetime.timedelta(days=days_input)

    return render(request, 'adminapp/DateTime.html', {'future_date': future_date})


def calculate_future_page(request):
    return render(request, 'adminapp/DateTime.html')


def get_time_details(request):
    timezones = pytz.all_timezones
    timezone_time = None
    error_message = None
    timezone_name = None

    if request.method == 'POST':
        timezone_name = request.POST.get('timezone')
        try:
            # Get the current time in UTC
            utc_now = datetime.utcnow()

            # Convert UTC time to the selected timezone
            selected_timezone = pytz.timezone(timezone_name)
            timezone_time = utc_now.replace(tzinfo=pytz.utc).astimezone(selected_timezone)

            # Format the timezone_time for better readability (optional)
            timezone_time = timezone_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')

        except pytz.UnknownTimeZoneError:
            error_message = "Invalid timezone selected. Please select a valid timezone."
        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"

    return render(request, 'adminapp/time.html', {
        'timezones': timezones,
        'timezone_time': timezone_time,
        'timezone_name': timezone_name,
        'error_message': error_message,

     })
from .forms import *
'''
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})
    '''

def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})





from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'adminapp/add_student.html', {'form': form})





#  ============== CSV TASK ===============

import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
matplotlib.use('Agg')

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # Read the CSV file
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)

        # Calculate total and average sales
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        # Add a 'Month' column and calculate monthly sales
        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()

        # Month names for labels
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%', startangle=90)
        plt.title('Sales Distribution Per Month')

        # Save the plot to a buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Convert to base64 to send to the template
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()

        # Pass data to the template
        context = {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'monthly_sales': monthly_sales.to_dict(),
            'chart': image_data,
        }
        return render(request, 'adminapp/chart.html', context)

    return render(request, 'adminapp/chart.html')

def feedback(request):
    return render(request,'adminapp/feedback.html')

from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page or feedback form

    else:
        form = FeedbackForm()  # Create a new form instance

    return render(request, 'feedback_form.html', {'form': form})
    return redirect('success')

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings

# Add Contact View
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_contacts')
    else:
        form = ContactForm()
    return render(request, 'adminapp/add_contact.html', {'form': form})


# View Contacts

def view_contacts(request):
    # Handling search
    search_query = request.GET.get('search', '')
    if search_query:
        contacts = Contact.objects.filter(
            name__icontains=search_query
        ) | Contact.objects.filter(
            email__icontains=search_query
        )
    else:
        contacts = Contact.objects.all()

    # Handling delete
    if 'delete_contact_id' in request.GET:
        contact_id = request.GET.get('delete_contact_id')
        contact = get_object_or_404(Contact, id=contact_id)
        contact.delete()
        return redirect('view_contacts')  # Redirect to refresh the page after deletion

    return render(request, 'adminapp/view_contacts.html', {'contacts': contacts})

def delete_contact(request, contact_id):
    # Get the contact object or return a 404 error if not found
    contact = get_object_or_404(Contact, id=contact_id)
    # Delete the contact
    contact.delete()
    # Redirect back to the view contacts page
    return redirect('view_contacts')


