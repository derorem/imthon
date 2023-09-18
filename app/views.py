from django.shortcuts import render, redirect
from app.models import Todo
def toddo(request):
    data={
        'todos':Todo.objects.all()
    }
    return render(request,'todo.html',data)

def __str__(self):
    return self.title


def delate(request,id,Post=None):
    if Post.git:
        title=Post.git('title')
        time=Post.git('time')
        docs=Post.git('docs')
        status=Post.git('status')
        Todo.objects.create(title=title,time=time,docs=docs,status=status)
        return redirect('/')
    data={
        'todos':Todo.objects.get(id=id)
    }
    return render(request,'delate.html',data)


def __str__(self):
    return self.title
def editodo(request,sher):
    if request.POST:
        title=request.POST.get('title')
        time=request.POST.get('time')
        docs=request.POST.get('docs')
        status=request.POST.get('status')
        Todo.objects.filter(id=sher)
        Todo.objects.update(title=title, time=time, docs=docs, status=status)
        return redirect('/')
    Data={
        'todo':Todo.objects.get(id=sher)
    }
    return render(request,'edit.html',Data)