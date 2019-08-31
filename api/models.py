from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from employee.models import Employee
from myproject import settings


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'financial'),
        (3, 'employee'),
    )
    id = models.AutoField(primary_key=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    REQUIRED_FIELDS = ['email',
                       'user_type']

    def __int__(self):
        return self.id


objects = UserManager()


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, user_type=None):
        user = self.model(
            email=self.normalize_email(email),
            user_type=user_type,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, user_type):
        user = self.create_user(
            email,
            password=password,
            user_type=user_type,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, user_type):
        user = self.create_user(
            email,
            password=password,
            user_type=user_type,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
