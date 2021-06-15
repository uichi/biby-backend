from django.urls import path
from . import views

app_name = 'red_list'

urlpatterns = [
    path('', views.Top.as_view(), name='animal'),
    path('rule', views.Rule.as_view(), name='rule'),
]
