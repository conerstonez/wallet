from rest_framework import serializers
# from djmoney.contrib.django_rest_framework import MoneyField

from wallet_app.models import *


class WalletUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password', 'username')

    # full_name = serializers.SerializerMethodField(method_name='get_full_name')

    # @staticmethod
    # def get_full_name(self, wallet_user: WalletUser):
    #     return wallet_user.get_full_name()


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['wallet_number', 'balance']


class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitCard
        fields = ['card_number', 'card_holder_name']
