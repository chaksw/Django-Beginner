

from django.urls import path
from scData import views

urlpatterns = [
    # path("scData/", views.index, name="index"),
    path("", views.index, name="index"),
    path('table/', views.scTable, name='scTable'),
    # path('importData/', views.importData, name='importData'),
]
