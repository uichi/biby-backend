from django.urls import include, path
from rest_framework import routers
from .views import CareCategoryViewSet,\
    PetViewSet,\
    PetCareLogViewSet,\
    PetOwnerGroupViewSet,\
    UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pets', PetViewSet)
router.register(r'pet_owner_group', PetOwnerGroupViewSet)
router.register(r'care_category', CareCategoryViewSet)
router.register(r'pet_care_log', PetCareLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
