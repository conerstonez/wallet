from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import WalletUserSerializer
from wallet_app.models import WalletUser


# Create your views here.


class UserViewSet(ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    # pagination_class = DefaultPageNumberPagination
    queryset = WalletUser.objects.all()
    serializer_class = WalletUserSerializer
    pass
