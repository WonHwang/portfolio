from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Introduction, Project
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib import auth

# 홈
def home(request):
    
    profiles = Profile.objects
    intros = Introduction.objects
    projects = Project.objects

    return render(request, 'home.html', {'profiles':profiles, 'intros':intros, 'projects':projects})

def edit(request):
    return render(request, 'edit.html')    

# 프로젝트 관리

def project_list(request):
    projects = Project.objects
    return render(request, 'project/project_list.html', {'projects' : projects})

def project_detail(request, pk):
    project_detail = get_object_or_404(Project, pk = pk)
    return render(request, 'project/project_detail.html', {'project' : project_detail})

def create_project(request):
    if request.method == 'POST':
        project = Project()
        project.title = request.POST['title']
        project.period = request.POST['period']
        project.body = request.POST['body']
        if request.FILES.get('image'):
            project.image = request.FILES['image']
        project.detail = request.POST['detail']
        project.save()
        return redirect('/detail/' + str(project.pk))
    else:
        return render(request, 'project/create_project.html')

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return render(request, 'home.html')

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.title = request.POST['title']
        project.period = request.POST['period']
        project.body = request.POST['body']
        if request.FILES.get('image'):
            project.image = request.FILES['image']
        project.detail = request.POST['detail']
        project.save()
        return redirect('/detail/' + str(project.pk))
    else:
        return render(request, 'project/project_edit.html', {'project' : project})

# 프로필 관리

def profile_list(request):
    profiles = Profile.objects
    return render(request, 'profile/profile_list.html', {'profiles' : profiles})

def create_profile(request):
    if request.method=='POST':
        profile = Profile()
        profile.body = request.POST['body']
        profile.save()
        return redirect('/profile_list/')
    else:
        return render(request, 'profile/create_profile.html')

def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method=='POST':
        profile.body = request.POST['body']
        profile.save()
        return redirect('/profile/detail/' + str(profile.pk))
    else:
        return render(request, 'profile/profile_edit.html', {'profile' : profile})

def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.delete()
    return redirect('/profile_list/')

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profile/profile_detail.html', {'profile' : profile})

# 인트로덕션 관리

def intro_list(request):
    intros = Introduction.objects
    return render(request, 'intro/intro_list.html', {'intros' : intros})

def create_intro(request):
    if request.method=='POST':
        intro = Introduction()
        intro.body = request.POST['body']
        intro.save()
        return redirect('/intro_list/')
    else:
        return render(request, 'intro/create_intro.html')

def intro_edit(request, pk):
    intro = get_object_or_404(Introduction, pk=pk)
    if request.method=='POST':
        intro.body = request.POST['body']
        intro.save()
        return redirect('/intro/detail/' + str(intro.pk))
    else:
        return render(request, 'intro/intro_edit.html', {'intro' : intro})

def intro_delete(request, pk):
    intro = get_object_or_404(Introduction, pk=pk)
    intro.delete()
    return redirect('/intro_list/')

def intro_detail(request, pk):
    intro = get_object_or_404(Introduction, pk=pk)
    return render(request, 'intro/intro_detail.html', {'intro' : intro})