from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
# Create your views here.


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContactFormView(FormView):
    # connect form class to form view class
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL ? where to go to after submit successfully
    # reverse() returns a string and reverse_lazy() returns an object
    # if using success_url, use reverse_lazy().
    success_url = reverse_lazy('classroom:thank_you')
    # What to do with form ?

    def form_valid(self, form):
        print(form.cleaned_data['name'])
        # ContactFormView(request.POST)
        return super().form_valid(form)
        # form.save()
