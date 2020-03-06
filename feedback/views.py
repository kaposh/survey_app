from django.shortcuts import render, redirect
from feedback.forms import ExampleForm, RegisterForm
from django.http import HttpResponse
from .models import Practice
from django.http import HttpResponseNotFound

# Create your views here.
def generic_form(request):
    form = ExampleForm()
    return render(request, 'feedback/form.html', {'form': form}, )

def specific_form(request, practiceid):
    form = ExampleForm()
    practices = Practice.objects.filter(practice_id=practiceid)
    if(not practices):
        return render(request, 'feedback/unregistered.html')
    else:
        return render(request, 'feedback/form.html', { 'practice': practices[0],'form': form}, )

def submit(request):
    return redirect("http://funweb.co.nz")

def register(request):
    form = RegisterForm()
    return render(request, 'feedback/register.html', {'form': form}, )

def registered(request):
    return HttpResponse("You have been registered")