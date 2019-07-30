from rest_framework import generics

from . import models
from . import serializers


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustUser.objects.all()
    serializer_class = serializers.UserSerializer