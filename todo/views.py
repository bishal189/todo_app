from django.shortcuts import render,redirect,get_object_or_404
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


def complete(request,pk):
    item=get_object_or_404(todo,pk=pk)
    item.is_completed=True
    item.save()
    return redirect('/')


def uncomplete(request,pk):
    item=get_object_or_404(todo,pk=pk)
    item.is_completed=False
    item.save()
    return redirect('/')





def edit_task(request,pk):
    get_task=get_object_or_404(todo,pk=pk)
    if request.method=="POST":
        get_data=request.POST['text']
        get_task.text_data=get_data
        get_task.save()
        return redirect('/')

    else:
        context={
            'get_task':get_task,
        }

    return render(request,'edit.html',context)



def delete(request,pk):
    get_data=get_object_or_404(todo,pk=pk)
    get_data.delete()
    return redirect('/')