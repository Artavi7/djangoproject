from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Welcome to Django Course!'
    return render(request, 'index.html', {
        'title' : title
    })

def about(request):
    username = 'Artavi'
    return render(request, 'about.html', {
        'username' : username
    })

def hello(request, username):
    
    return HttpResponse("<h2>Dios primero</h2><br> <h3>Hola %s </h3>" % username )

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects' : projects
    })

def tasks(request):
    #task = Task.objects.get(id=id) es lo mismo q lo de abajo
    #task = get_object_or_404(Task, id=id)
    #task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks': tasks
    })