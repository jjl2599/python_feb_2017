from django.shortcuts import render, redirect
from . models import Course
# Create your views here.
def index(request):
    context = {
    "courses": Course.objects.all(),
    }
    return render(request, 'main/index.html', context)

def courses(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def deletepage(request, id):
    context = {
        "course": Course.objects.get(id=id),
    }
    return render(request, 'main/delete.html', context)

def delete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect ('/')
