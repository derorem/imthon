from django.shortcuts import render
from app.models import Todo
def todo(request):
    data={
        'todos':Todo.objects.all()
    }
    return render(request,'todo.html',data)

def __str__(self):
    return self.title
