from django.urls import include, path
# from rest_framework import routers
from .views import RegisterViewSet

# router = routers.DefaultRouter()
# router.register(r'users/register', RegisterViewSet)

urlpatterns = [
    path('users/register', RegisterViewSet.as_view()),
]