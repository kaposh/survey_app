from django.shortcuts import render, redirect
from feedback.forms import ExampleForm
from django.http import HttpResponse

# Create your views here.
def form(request):
    form = ExampleForm()
    return render(request, 'feedback/form.html', {'form': form}, )

def submit(request):
    return HttpResponse("Submited")

#def success(request):
#    return HttpResponse("Hello, world. You're at the polls index.")