from django.shortcuts import render

from rest_framework import generics

from . import models
from . import serializers

from .models import CustomUser

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer





def verification(request, external_id):
    employee = CustomUser.objects.get(external_id=external_id)
    employee.is_verified = True
    employee.save()
    return HttpResponseRedirect(reverse('index'))