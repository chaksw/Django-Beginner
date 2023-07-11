from django import forms
from .models import Project, Functionality, Load, TestPlan, TestException
class projectModalForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        
class functionalityModalForm(forms.ModelForm):
    class Meta:
        model = Functionality
        fields = "__all__"
        
class loadModalForm(forms.ModelForm):
    class Meta:
        model = Load
        fields = "__all__"