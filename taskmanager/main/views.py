from django.shortcuts import render, redirect
from .models import task
from .forms import taskForm


def index(request):
    tasks = task.objects.order_by('-id')
    return render(request, 'taskmanager/index.html', {'title': 'главная страница сайта', 'tasks': tasks })


def about(request):
    return render(request, 'taskmanager/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма Была Неверной'



    form = taskForm()
    context ={
        'form': form,
        'error': error
    }
    return render(request, 'taskmanager/create.html', context)


