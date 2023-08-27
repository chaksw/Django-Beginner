from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from rest_framework import viewsets
from .models import Client, Note
from .serializers import ClientSerializer, NoteSerializer
from team.models import Team
from lead.models import Lead
# Create your views here.


class ClientPagination(PageNumberPagination):
    page_size = 10


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'contact_person', 'email', 'phone', 'website')
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
        return self.queryset.filter(team=team).filter(client_id=client_id)

# trigger when POST method raised in front-end


@api_view(['POST'])
def convert_lead_to_client(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']
    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        raise Http404
    client = Client.objects.create(team=team, name=lead.company, contact_person=lead.contact_person,
                                   email=lead.email, phone=lead.phone, website=lead.website, created_by=request.user)
    return Response()


@api_view(['POST'])
def delete_client(request, client_id):
    team = Team.objects.filter(members__in=[request.user]).first()
    client = team.clients.filter(pk=client_id)
    client.delete()
    msg = 'The client was deleted'
    return Response({'Message': msg})
