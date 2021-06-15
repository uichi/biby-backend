from django.urls import path
from . import views

app_name = 'animal_organization'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
]
