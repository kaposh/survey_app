from django.shortcuts import render, redirect
from feedback.forms import ExampleForm
from django.http import HttpResponse

# Create your views here.
def success(request):
    form = ExampleForm()
    return render(request, 'feedback/success.html', {'form': form}, )


#def success(request):
#    return HttpResponse("Hello, world. You're at the polls index.")