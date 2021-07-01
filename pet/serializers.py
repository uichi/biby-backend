from rest_framework.serializers import ModelSerializer, CharField, PrimaryKeyRelatedField
from .models import CareCategory, Pet, PetCareLog, PetOwnerGroup
from django.contrib.auth import get_user_model

User = get_user_model()


class PetSerializer(ModelSerializer):
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


class CareCategorySerializer(ModelSerializer):
    class Meta:
        model = CareCategory
        fields = (
            'id',
            'name',
            'icon',
            'input_type',
            'unit',
            'is_daily_routine',
            'user')


class PetCareLogSerializer(ModelSerializer):
    care_category_pk = PrimaryKeyRelatedField(
        queryset=CareCategory.objects.all(), source='care_category', write_only=True
    )
    user_pk = PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    pet_pk = PrimaryKeyRelatedField(
        queryset=Pet.objects.all(), source='pet'
    )

    class Meta:
        model = PetCareLog
        fields = (
            'id',
            'date_time',
            'integer',
            'float',
            'text',
            'checkbox',
            'care_category',
            'care_category_pk',
            'memo',
            'user_pk',
            'pet_pk')
        depth = 1


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
