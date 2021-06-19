from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission
from .models import CareCategory, Pet, PetCareLog, PetOwnerGroup
from .serializers import CareCategorySerializer,\
    PetSerializer,\
    PetCareLogSerializer,\
    PetOwnerGroupSerializer,\
    UserSerializer


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_fields = (
        'id',
        'name',
        'image',
        'gender',
        'birthday',
        'welcome_day',
        'share_id',
        'is_heaven')
    permission_classes = (IsSuperUser, )


class PetOwnerGroupViewSet(viewsets.ModelViewSet):
    queryset = PetOwnerGroup.objects.all()
    serializer_class = PetOwnerGroupSerializer
    filter_fields = ('user', 'pet')
    permission_classes = (IsSuperUser, )


class CareCategoryViewSet(viewsets.ModelViewSet):
    queryset = CareCategory.objects.all()
    serializer_class = CareCategorySerializer
    filter_fields = (
        'name',
        'icon',
        'input_type',
        'unit',
        'is_daily_routine',
        'pet')
    permission_classes = (IsSuperUser, )


class PetCareLogViewSet(viewsets.ModelViewSet):
    queryset = PetCareLog.objects.all()
    serializer_class = PetCareLogSerializer
    filter_fields = (
        'integer',
        'float',
        'text',
        'checkbox',
        'care_category',
        'memo')
    permission_classes = (IsSuperUser, )


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser, )
