from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


def home_view(request):
    return HttpResponse("HOME PAGE")
