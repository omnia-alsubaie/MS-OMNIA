from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Project
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def projects(request):
    return HttpResponse("TEST OMNIA")

def index(request):
    return redirect('projects')

def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Project.objects.create(
            title=title,
            description=description,
            user=request.user
        )

        return redirect('projects')

    return render(request, 'create_project.html')



def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk, user=request.user)
    return render(request, 'project_detail.html', {'project': project})



def edit_project(request, pk):
    project = get_object_or_404(Project, id=pk, user=request.user)

    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.save()
        return redirect('projects')

    return render(request, 'edit_project.html', {'project': project})



def delete_project(request, pk):
    project = get_object_or_404(Project, id=pk, user=request.user)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'project_confirm_delete.html', {'project': project})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('projects')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form}) 
def projects(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects.html', {'projects': projects})

def projects(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects.html', {'projects': projects})