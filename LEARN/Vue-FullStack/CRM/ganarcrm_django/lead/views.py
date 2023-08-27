from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from rest_framework.views import APIView, DefaultSchema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Lead
from .serializers import LeadSerializer
from team.models import Team
# Create your views here.
# print(type(APIView.authentication_classes))
# print(APIView.authentication_classes)


class LeadPagination(PageNumberPagination):
    page_size = 10


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    pagination_class = LeadPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('company', 'contact_person', 'email', 'phone', 'website')
    # action when we create a lead

    def perform_create(self, serializer):
        # search the team (contain current user) (as per client creation[input])
        team = Team.objects.filter(members__in=[self.request.user]).first()
        # return serializer.save(created_by = self.request.user)
        return serializer.save(team=team, created_by=self.request.user)
        # return serializer.save(team = team)

    def perform_update(self, serializer):
        obj = self.get_object()
        member_id = self.request.data['assigned_to']
        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()

    def get_queryset(self):
        # filter will return a list, so using first() to return the first object matched by the queryset
        team = Team.objects.filter(members__in=[self.request.user]).first()
        # return self.queryset.filter(team = team, created_by = self.request.user)
        return self.queryset.filter(team=team)


@api_view(['POST'])
def delete_lead(request, lead_id):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead = team.leads.filter(pk=lead_id)
    lead.delete()
    msg = 'The lead was deleted'
    return Response({'Message': msg})
