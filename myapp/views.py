from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    
    return HttpResponse("<h2>Dios primero</h2><br> <h3>Hola %s </h3>" % username )

def about(request):
    return HttpResponse("About")

def projects(resquest):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(resquest, id):
    #task = Task.objects.get(id=id) es lo mismo q lo de abajo
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)