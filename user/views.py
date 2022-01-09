from rest_framework.generics import GenericAPIView, ListApiView
from rest_framework.permissions import AllowAny

from user.models import Account
from .serializers import UserSerializer, RegisterUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import dumps
from django.template.loader import get_template
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListViewSet(ListApiView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
