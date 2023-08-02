

from django.http import HttpResponse
from django.shortcuts import render
from todo.models import todo


def home(request):
    incomplete_data=todo.objects.filter(is_completed=False)
    complete_data=todo.objects.filter(is_completed=True)
    task={
        'incomplete_data':incomplete_data,
        'complete_data':complete_data,
    }
    print(incomplete_data)
    return render(request,'home.html',task)