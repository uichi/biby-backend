from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission
from .models import CareCategory, Pet, PetCareLog, PetOwnerGroup
from .serializers import CareCategorySerializer,\
    PetSerializer,\
    PetCareLogSerializer,\
    PetOwnerGroupSerializer,\
    UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    # permission_classes = (IsSuperUser, )
    parser_classes = (JSONParser, MultiPartParser)
    filter_fields = ('name',)

    def perform_create(self, serializer):
        pet = serializer.save()
        pet_owner_group = PetOwnerGroup(user=self.request.user, pet=pet)
        pet_owner_group.save()


class PetOwnerGroupViewSet(viewsets.ModelViewSet):
    queryset = PetOwnerGroup.objects.all()
    serializer_class = PetOwnerGroupSerializer
    filter_fields = ('user', 'pet')
    # permission_classes = (IsSuperUser, )


class CareCategoryViewSet(viewsets.ModelViewSet):
    queryset = CareCategory.objects.all()
    serializer_class = CareCategorySerializer
    filter_fields = (
        'id',
        'name',
        'icon',
        'input_type',
        'unit',
        'is_daily_routine',
        'user')
    # permission_classes = (IsSuperUser, )


class PetCareLogViewSet(viewsets.ModelViewSet):
    queryset = PetCareLog.objects.all()
    serializer_class = PetCareLogSerializer
    filter_fields = (
        'date_time',
        'integer',
        'float',
        'text',
        'checkbox',
        'care_category',
        'memo',
        'pet',
    )
    # permission_classes = (IsSuperUser, )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsSuperUser, )