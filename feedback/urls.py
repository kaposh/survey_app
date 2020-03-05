from django.urls import path

from . import views

app_name = 'feedback'
urlpatterns = [
    path('form', views.form, name='form'),
    path('submit_survey', views.submit, name='submit'),
]