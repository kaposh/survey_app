from django.urls import path

from . import views

app_name = 'feedback'
urlpatterns = [
    path('', views.generic_form, name='form'),
    path('submit_survey', views.submit, name='submit'),
    path('register_form', views.register, name='register'),
    path('registered', views.registered, name='registered'),
    path('<str:practiceid>', views.specific_form, name='form'),

]