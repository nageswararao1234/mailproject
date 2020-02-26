from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    mobile = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    external_id = models.CharField(max_length=100)

    def __str__(self):
        return self.email