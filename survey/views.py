from django.shortcuts import render, redirect
from feedback.forms import ExampleForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html' )
#    return HttpResponse("Hello, world. You're at the polls index.")


#def success(request):
