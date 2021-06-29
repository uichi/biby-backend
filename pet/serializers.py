from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, CharField
from .models import CareCategory, Pet, PetCareLog, PetOwnerGroup
from django.contrib.auth import get_user_model

User = get_user_model()


class PetSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = (
            'id',
            'name',
            'image',
            'gender',
            'birthday',
            'welcome_day',
            'share_id',
            'is_heaven')


class PetOwnerGroupSerializer(ModelSerializer):

    class Meta:
        model = PetOwnerGroup
        fields = ('pet',)
        depth = 1


class CareCategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CareCategory
        fields = (
            'name',
            'icon',
            'input_type',
            'unit',
            'is_daily_routine',
            'user')


class PetCareLogSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PetCareLog
        fields = (
            'integer',
            'float',
            'text',
            'checkbox',
            'care_category',
            'memo')


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
