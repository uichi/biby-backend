from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterUserSerializer(ModelSerializer):
    password_confirm = CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', )
        password = attrs.get('password', )
        password_confirm = attrs.get('password_confirm', )
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                {'email': 'Email is already in use'})
        if password != password_confirm:
            raise ValidationError(
                {'password': 'Password must math.'})
        del attrs['password_confirm']
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
