from django.contrib import admin
from .models import Project, Functionality, Load, TestPlan, TestException
from django_object_actions import DjangoObjectActions, action
from django.utils.translation import ngettext
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
# Register your models here.
admin.site.site_header = 'SCGA Admin Panel'

# add import button
# class ImportAdmin(DjangoObjectActions, admin.ModelAdmin):
#     def imports(modeladmin, request, queryset):
#         modeladmin.message_user(
#             request,
#             ngettext(
#                 '%d record was successfully imported.',
#                 '%d records were successfully imported.',
#             )
#         )
#     changelist_actions = ('imports',)


class MyModelModelAdmin(ExtraButtonsMixin, admin.ModelAdmin):

    @button(permission='demo.add_demomodel1',
            change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    def refresh(self, request):
        self.message_user(request, 'refresh called')
        # Optional: returns HttpResponse
        return HttpResponseRedirectToReferrer(request)

    @button(html_attrs={'style': 'background-color:#DC6C6C;color:black'})
    def confirm(self, request):
        def _action(request):
            pass

        return confirm_action(self, request, _action, "Confirm action",
                              "Successfully executed", )

    @link(href=None,
          change_list=False,
          html_attrs={'target': '_new', 'style': 'background-color:var(--button-bg)'})
    def search_on_google(self, button):
        original = button.context['original']
        button.label = f"Search '{original.name}' on Google"
        button.href = f"https://www.google.com/?q={original.name}"

    @view()
    def select2_autocomplete(self, request):
        return JsonResponse({})

    @view(http_basic_auth=True)
    def api4(self, request):
        return HttpResponse("Basic Authentication allowed")

    @view(decorators=[csrf_exempt, xframe_options_sameorigin])
    def preview(self, request):
        if request.method == "POST":
            return HttpResponse("POST")
        return HttpResponse("GET")


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


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [FunctionalityInline]


@admin.register(Functionality)
class FunctionalityAdmin(admin.ModelAdmin):
    model = Functionality
    inlines = [LoadInline]
    list_display = ('func', 'Project')
    fields = ('func', 'Project')


@admin.register(Load)
class LoadAdmin(admin.ModelAdmin):
    model = Load
    inlines = [TestPlanInline]
    list_display = ('load', 'Func')
    fields = ('load', 'Func')


@admin.register(TestPlan)
class TestPlanAdmin(admin.ModelAdmin):
    model = TestPlan
    inlines = [TestExceptionInline]
    empty_value_display = '-empty-'  # The string to display in lieu of an empty value
    # a list_display tuple of field names to display, as columns, on the change list page for the object
    list_display = ('func', 'level', 'process', 'fName',
                    'swLoad', 'analyst', 'site', 'startDate')
    # a list_filter tuple of field names that will be displayed in the right sidebar of the change list page of the admin
    list_filter = ('func', 'level', 'process', 'fName',
                   'swLoad', 'analyst', 'site', 'startDate')
    # a search_fields tuple of field names that will be searched whenever somebody submits a search query in that text box
    search_fields = ('func', 'level', 'process', 'fName',
                     'swLoad', 'analyst', 'site', 'startDate')
    fieldsets = [
        ('Test Plan', {'fields': ['func', 'level', 'process', 'fName',
                                  'swLoad', 'analyst', 'site', 'startDate']}),
        ("Coverage Result", {
            "classes": ["collapse"],
            "fields": ["mcdcCoverage", "analysisCoverage", "totalScCoverage", "coveredBranches", "coveredPairs", "coveredStatements", "totalBranches", "totalPairs", "totalStatements",
                       "overSight", "tech", "nonTech", "processDefect"]},)
    ]


@admin.register(TestException)
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
        ('Test Exception', {'fields': ['module', 'function', 'SWline',
         'InsSWline', 'reqTag', 'analyst', 'ucClassification', 'testPlan']}),
        ("Analysis Fields", {
            "classes": ["collapse"],
            "fields": ["analysisSummary", "correctiveAction", "issue", "applicable"]},),
    ]
    list_display_links = ["function"]


# register all models imported from models using admin.site.register()
# admin.site.register(Project, ProjectAdmin)
# # admin.site.register(Certification)
# admin.site.register(Functionality, FunctionalityAdmin)
# admin.site.register(Load, LoadAdmin)
# admin.site.register(TestPlan, TestPlanAdmin)
# admin.site.register(TestException, TestExceptionAdmin)
