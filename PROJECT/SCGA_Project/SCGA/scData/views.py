from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import projectModalForm, functionalityModalForm, loadModalForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'scData/index.html'


def import_view(request):
    if request.method == 'POST':
        projectForm = projectModalForm(request.POST, prefix='projectModal')
        funcForm = functionalityModalForm(request.POST, prefix='functionalityModal')
        loadForm = loadModalForm(request.POST, prefix='loadModal')
        if projectForm.is_valid() and funcForm.is_valid() and loadForm.is_valid():
            projectForm.save()
            print(projectForm.cleaned_data)
    else:
        projectForm = projectModalForm(prefix='projectModal')
        funcForm = functionalityModalForm(prefix='functionalityModal')
        loadForm = loadModalForm(prefix='loadModal')
        
    return render(request, 'admin/base.html', context={'projectForm':projectForm, 'funcForm':funcForm, 'loadForm':loadForm})