from django.contrib import admin
from .models import Project, Functionality, Load, TestPlan, TestException
# Register your models here.
admin.site.site_header = 'SCGA Administration'


def import_xlms(modeladmin, request, queryset):
    pass


admin.site.add_action(import_xlms, 'import_xlms')


class TestExceptionInline(admin.TabularInline):
    model = TestException


class TestExceptionAdmin(admin.ModelAdmin):
    model = TestException
    empty_value_display = '-empty-'  # The string to display in lieu of an empty value
    list_display = ('note', 'module', 'function', 'line',
                    'reqTag', 'analyst', 'ucClassification')
    list_filter = ('note', 'module', 'function', 'line',
                   'reqTag', 'analyst', 'ucClassification')
    search_fields = ('note', 'module', 'function', 'line',
                     'reqTag', 'analyst', 'ucClassification')


class TestPlanInline(admin.TabularInline):
    # The name of a DateField or DateTimeField in your model
    # date_hierarchy = 'imported_date'
    model = TestPlan


class TestPlanAdmin(admin.ModelAdmin):
    model = TestPlan
    empty_value_display = '-empty-'  # The string to display in lieu of an empty value
    # a list_display tuple of field names to display, as columns, on the change list page for the object
    list_display = ('level', 'process', 'fName', 'func',
                    'swLoad', 'analyst', 'site', 'testException', 'startDate')
    # a list_filter tuple of field names that will be displayed in the right sidebar of the change list page of the admin
    list_filter = ('level', 'process', 'fName', 'func',
                   'swLoad', 'analyst', 'site', 'testException', 'startDate')
    # a search_fields tuple of field names that will be searched whenever somebody submits a search query in that text box
    search_fields = ('level', 'process', 'fName', 'func',
                     'swLoad', 'analyst', 'site', 'testException', 'startDate')
    # a Inlines display of related objects on the same page as the parent object
    # inlines = [TestExceptionInline]


class LoadInline(admin.TabularInline):
    model = Load
    # date_hierarchy = 'imported_date'


class LoadAdmin(admin.ModelAdmin):
    model = Load
    inlines = [TestPlanInline]
    list_display = ('load', 'Func')
    fields = ('load', 'Func')


class FunctionalityInline(admin.TabularInline):
    model = Functionality
    # date_hierarchy = 'imported_date'


class FunctionalityAdmin(admin.ModelAdmin):
    model = Functionality
    inlines = [LoadInline]
    list_display = ('func', 'Project')
    fields = ('func', 'Project')


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [FunctionalityInline]
    # date_hierarchy = 'imported_date'


# register all models imported from models using admin.site.register()
admin.site.register(Project, ProjectAdmin)
# admin.site.register(Certification)
admin.site.register(Functionality, FunctionalityAdmin)
admin.site.register(Load, LoadAdmin)
admin.site.register(TestPlan, TestPlanAdmin)
admin.site.register(TestException, TestExceptionAdmin)
