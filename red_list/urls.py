from django.urls import path
from . import views

app_name = 'red_list'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('rule', views.Rule.as_view(), name='rule'),
]
