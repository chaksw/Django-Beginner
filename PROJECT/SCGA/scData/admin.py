from django.contrib import admin

# Register your models here.
from .models import Project, Functionality, Load, TestPlan, TestException
# register all models imported from models using admin.site.register()
admin.site.register(Project)
# admin.site.register(Certification)
admin.site.register(Functionality)
admin.site.register(Load)
admin.site.register(TestPlan)
admin.site.register(TestException)
