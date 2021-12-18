from django.db.models import CharField, EmailField, BooleanField, DateTimeField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        username = self.model.normalize_username(username)
        email = self.model.normalize_username(email)
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = CharField(
        _('username'),
        max_length=150,
        unique=False,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
    )
    first_name = CharField(_('first name'), max_length=30, blank=True)
    last_name = CharField(_('last name'), max_length=150, blank=True)
    email = EmailField(_('email address'), unique=True, blank=True)
    is_admin = BooleanField(default=False)

    is_staff = BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = BooleanField(
        _('active'),
        default=False,
        help_text=_(
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.')
        ,
    )
    date_joined = DateTimeField(_('date joined'), default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
