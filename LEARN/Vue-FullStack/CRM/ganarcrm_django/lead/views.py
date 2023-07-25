from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView, DefaultSchema
from .models import Lead
from .serializers import LeadSerializer
# Create your views here.
print(type(APIView.authentication_classes))
print(APIView.authentication_classes)

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(created_by = self.request.user)