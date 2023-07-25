from rest_framework import serializers

from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            'id',
            'company',
            'contact_person',
            'eamil',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'created_by',
            'created_at',
            'modified_at',
        )
