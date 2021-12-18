from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from user.models import Account
from .serializers import RegisterUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import dumps
from django.template.loader import get_template
from django.core.mail import send_mail


class RegisterViewSet(GenericAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            current_site = get_current_site(self.request)
            domain = current_site.domain
            context = {
                'protocol': 'https' if self.request.is_secure() else 'http',
                'domain': domain,
                'token': dumps(account.pk),
                'user': account.username,
            }
            subject_template = get_template('user/mail_templates/create_user/subject.txt')
            subject = subject_template.render(context)

            message_template = get_template('user/mail_templates/create_user/message.txt')
            message = message_template.render(context)

            send_mail(subject, message, from_email=None, recipient_list=[account.email])

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
