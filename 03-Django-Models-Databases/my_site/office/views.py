from django.shortcuts import render
from . import models
# Create your views here.


def list_patients(request):
    all_patient = models.Patient.objects.all()
    context = {'patients': all_patient}
    return render(request, 'office/list.html', context=context)
