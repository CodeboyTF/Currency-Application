from . import views
from django.urls import path


app_name = 'Calculator'

urlpatterns = [
    path('', views.index, name='index')
]