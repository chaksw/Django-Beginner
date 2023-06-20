from django.contrib import admin
from .models import Project, Functionality, Load, TestPlan, TestException
# Register your models here.
admin.site.site_header = 'SCGA Admin Panel'

# add reset password



class FunctionalityInline(admin.TabularInline):
    model = Functionality
    
class LoadInline(admin.TabularInline):
    model = Load
    
class TestPlanInline(admin.TabularInline):
    # The name of a DateField or DateTimeField in your model
    # date_hierarchy = 'imported_date'
    model = TestPlan
    
class TestExceptionInline(admin.TabularInline):
    model = TestException


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [FunctionalityInline]


class FunctionalityAdmin(admin.ModelAdmin):
    model = Functionality
    inlines = [LoadInline]
    list_display = ('func', 'Project')
    fields = ('func', 'Project')    

class LoadAdmin(admin.ModelAdmin):
    model = Load
    inlines = [TestPlanInline]
    list_display = ('load', 'Func')
    fields = ('load', 'Func')


class TestPlanAdmin(admin.ModelAdmin):
    model = TestPlan
    inlines = [TestExceptionInline]
    empty_value_display = '-empty-'  # The string to display in lieu of an empty value
    # a list_display tuple of field names to display, as columns, on the change list page for the object
    list_display = ('func','level', 'process', 'fName', 
                    'swLoad', 'analyst', 'site', 'startDate')
    # a list_filter tuple of field names that will be displayed in the right sidebar of the change list page of the admin
    list_filter = ('func','level', 'process', 'fName', 
                    'swLoad', 'analyst', 'site', 'startDate')
    # a search_fields tuple of field names that will be searched whenever somebody submits a search query in that text box
    search_fields = ('func','level', 'process', 'fName', 
                    'swLoad', 'analyst', 'site', 'startDate')
    fieldsets = [
        ('Test Plan', {'fields': ['func','level', 'process', 'fName',
                            'swLoad', 'analyst', 'site', 'startDate']}),
        ("Coverage Result", {
            "classes":["collapse"],
            "fields": ["mcdcCoverage", "analysisCoverage", "totalScCoverage", "coveredBranches", "coveredPairs", "coveredStatements", "totalBranches", "totalPairs", "totalStatements",
                       "overSight", "tech", "nonTech", "processDefect"]},)      
    ]
    
    
class TestExceptionAdmin(admin.ModelAdmin):
    model = TestException
    empty_value_display = '-empty-'  # The string to display in lieu of an empty value
    list_display = ('id', 'module', 'function', 'SWline', 'InsSWline',
                    'reqTag', 'analyst', 'ucClassification', 'testPlan')
    list_filter = ('id', 'module', 'function', 'SWline', 'InsSWline',
                    'reqTag', 'analyst', 'ucClassification', 'testPlan')
    search_fields = ('id', 'module', 'function', 'SWline', 'InsSWline',
                    'reqTag', 'analyst', 'ucClassification', 'testPlan')
    fieldsets = [
        ('Test Exception', {'fields': ['module', 'function', 'SWline', 'InsSWline', 'reqTag', 'analyst', 'ucClassification', 'testPlan']}),
        ("Analysis Fields", {
            "classes": ["collapse"],
            "fields": ["analysisSummary", "correctiveAction", "issue", "applicable"]},),
    ]
    list_display_links = ["function"]
    
    

# register all models imported from models using admin.site.register()
admin.site.register(Project, ProjectAdmin)
# admin.site.register(Certification)
admin.site.register(Functionality, FunctionalityAdmin)
admin.site.register(Load, LoadAdmin)
admin.site.register(TestPlan, TestPlanAdmin)
admin.site.register(TestException, TestExceptionAdmin)
