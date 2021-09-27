"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pet.urls import router as pet_router
from blog.urls import router as blog_router


class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for extending url routes from another router.
    """
    def extend(self, app_router):
        """
        Extend the routes with url routes of the passed in router.

        Args:
             app_router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(app_router.registry)


router = DefaultRouter()
router.extend(pet_router)
router.extend(blog_router)

urlpatterns = [
    path('kawausoadmin/', admin.site.urls),
    path('red_list/', include('red_list.urls')),
    path('', include('animal_organization.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('user.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]

