from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Functionality, Load, TestPlan, TestException

# Create your views here.
def index(request):
    projects = Project.objects.all()
    functions = Functionality.objects.all()
    loads = Load.objects.all()
    testPlans = TestPlan.objects.all()
    testExceptions = TestException.objects.all()
    return render(request, 'index.html')


def importData(request):
    projects = Project(proejct=request.POST['project'])
    functions = Functionality(func=request.POST['function'])
    loads = Load(load=request.POST['load'])
    projects.save()
    functions.save()
    loads.save()
        
    return redirect('admin/base.html')