from django.urls import path
from . import views

urlpatterns = [
    # /hr/
    path('', views.index, name='index')
]