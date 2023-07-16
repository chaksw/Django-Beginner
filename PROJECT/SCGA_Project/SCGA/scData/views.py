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
        # projects = Project(id=2, proejct=request.POST['project'])
        # # functions = Functionality(func=request.POST['function'])
        # loads = Load(id=2, load=request.POST['load'])
        # projects.save()
        # # functions.save()
        # print(loads)
        # loads.save()

    return redirect('table/')
