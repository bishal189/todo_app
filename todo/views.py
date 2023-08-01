from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo

# Create your views here.

def add_task(request):
    print(request.method)
    if request.method == 'POST':
        print('post method')
        text=request.POST['text']
        data=todo(text_data=text)
        data.save()
    return redirect('/') 
    # return HttpResponse('hello world')
