from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns=[
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
    path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randompagelogic/', views.randompagelogic, name='randompagelogic'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('get_time_details/', views.get_time_details, name='get_time_details'),
    path('calculate_future_date/', views.calculate_future_date, name='calculate_future_date'),
    path('calculate_future_page/', views.calculate_future_page, name='calculate_future_page'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('logout/', views.logout, name='logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('generate/', views.upload_file, name='upload_file'),
    path('feedback/', views.feedback, name='feedback'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('<int:pk>/delete/', views.delete_contact, name='delete_contact'),
]
