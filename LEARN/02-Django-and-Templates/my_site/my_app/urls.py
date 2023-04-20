from . import views
from django.urls import path, include

# register the app namespace
# URL names
app_name = 'my_app'

urlpatterns = [
    path('', views.exmaple_view, name='example'),
    path('variable/', views.variable_view, name='variable')
]
