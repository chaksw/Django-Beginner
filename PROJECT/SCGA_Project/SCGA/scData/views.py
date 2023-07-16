from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Functionality, Load, TestPlan, TestException

# Create your views here.


def index(request):
    projects = Project.objects.all()
    functions = Functionality.objects.all()
    loads = Load.objects.all()
    testPlans = TestPlan.objects.all()
    testExceptions = TestException.objects.all()
    return render(request, 'index.html', {'projects': projects, 'functions': functions, 'loads': loads, 'testPlans': testPlans, 'testExceptions': testExceptions})


def scTable(request):
    projects = Project.objects.all()
    functions = Functionality.objects.all()
    loads = Load.objects.all()
    testPlans = TestPlan.objects.all()
    testExceptions = TestException.objects.all()
    return render(request, 'scTable.html', {'projects': projects, 'functions': functions, 'loads': loads, 'testPlans': testPlans, 'testExceptions': testExceptions})


def importData(request):
    print('request is running')
    if request.method == "POST":
        print("request: " + str(request.POST))
        projects = Project(project=request.POST.get('project'))
        functions = Functionality(func=request.POST.get('function'))
        loads = Load(load=request.POST.get('load'))
        projects.save()
        functions.save()
        loads.save()

    return redirect('table/')
