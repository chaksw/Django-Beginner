from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, DeleteView, UpdateView
from .forms import ContactForm
from classroom.models import Teacher
# Create your views here.


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


# CreateView
class TeacherCreateView(CreateView):
    # once defined model = Teacher to connect to model, django will look for the template 
    # named "modelname_form.html
    # just like the definition of template_name = 'classroom/teacher_form.html'
    # also when u hit the submit button, it's will automatically hit save() after all the field are validated.
    
    model = Teacher # connect to a model(database)
    # fields = ['first_name', 'last_name'] # connect to data attribute
    fields = '__all__'
    # reverse to another template after submit, 'thank_you` is name of path defined in urls
    success_url = reverse_lazy('classroom:list_teacher') 


class TeacherListView(ListView):
    # model_list.html
    model = Teacher
    # Grab instances in model and set the query view
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY using primary key
    model = Teacher
    # PK --> {{ teacher }}
    
class TeacherUpdateView(UpdateView):
    # SHARE the model_form.html from HTML template that CreateView also uses, and it looks a lot like create view as far as attributes concerned, but we can limit the field upon updating
    model = Teacher
    fields = ['last_name', 'first_name']
    # fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher') 
    

class TeacherDeleteView(DeleteView):
    model = Teacher
    # default template name:
    # model_confirm_delete.html
    success_url = reverse_lazy('classroom:list_teacher') 

class ContactFormView(FormView):
    # connect form class to form view class
    form_class = ContactForm # connect to form
    template_name = 'classroom/contact.html' # connect to template

    # success URL ? where to go to after submit successfully
    # reverse() returns a string and reverse_lazy() returns an object
    # if using success_url, use reverse_lazy().
    success_url = reverse_lazy('classroom:thank_you')
    # What to do with form ?
    def form_valid(self, form): # if form is valid, data created from front-end will be save in cleaned_data dictionary
        print(form.cleaned_data['name'])
        # ContactFormView(request.POST)
        return super().form_valid(form)
        # form.save()
