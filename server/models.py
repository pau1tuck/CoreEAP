from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=128, unique=False, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    company_name = models.CharField(max_length=256, blank=True)  
    city = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=128, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    last_visit = models.DateTimeField(auto_now=True, editable=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = u'User'
        verbose_name_plural = u'Users'

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.username, self.email, self.first_name, self.last_name, self.company_name, self.city, self.country)