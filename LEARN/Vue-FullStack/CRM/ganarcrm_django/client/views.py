from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Client, Note
from .serializers import ClientSerializer, NoteSerializer
from team.models import Team
# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    # action when we create a lead
    def perform_create(self, serializer):
        # search the team (contain current user) (as per client creation[input])
        team = Team.objects.filter(members__in=[self.request.user]).first()
        # return serializer.save(created_by = self.request.user)
        return serializer.save(team=team, created_by=self.request.user)
        # return serializer.save(team = team)

    # def perform_update(self, serializer):
    #     obj = self.get_object()

    #     serializer.save()

    def get_queryset(self):
        # filter will return a list, so using first() to return the first object matched by the queryset
        team = Team.objects.filter(members__in=[self.request.user]).first()
        # return self.queryset.filter(team = team, created_by = self.request.user)
        return self.queryset.filter(team=team)


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
    def perform_create(self, serializer):
         # search the team (contain current user) (as per client creation[input])
        team = Team.objects.filter(members__in=[self.request.user]).first()
        
        client_id = self.request.data['client_id']
        # return serializer.save(created_by = self.request.user)
        return serializer.save(team=team, created_by=self.request.user, client_id=client_id)
    
    def get_queryset(self):
        # filter will return a list, so using first() to return the first object matched by the queryset
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.GET.get('client_id')
        # return self.queryset.filter(team = team, created_by = self.request.user)
        return self.queryset.filter(team=team).filter(client_id =client_id)