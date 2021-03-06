from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(unique=False, null=False, max_length=50)
    last_name = models.CharField(unique=False, null=False, max_length=50)
    age = models.IntegerField(null=False)
    cpf = models.CharField(unique=True, null=False, max_length=11)
    phone = models.CharField(unique=True, max_length=13)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(unique=False, blank=True, null=True, max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
