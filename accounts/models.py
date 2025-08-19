import email

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from unicodedata import normalize

class UserManager(BaseUserManager):
    def create_user(
            self, username,email, password=None,
            first_name=None, last_name=None,
            is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        if not password:
            raise ValueError('Users must have a password')

        user_obj = self.model(
        email = self.normalize_email(email),
    )
        user_obj.set_password(password)
        user_obj.first_name = first_name
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin

        user_obj.save(using=self._db)

        return user_obj

    def create_superuser(self, username, email, password,):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_active=True,

        )

class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=255,
        unique=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=255,
        unique=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        null=True,
    )
    joined_date = models.DateTimeField(
        auto_now_add=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin