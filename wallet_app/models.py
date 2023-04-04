from enum import Enum
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class Account(models.Model):
    bank = models.CharField(max_length=20, default=None)
    account_number = models.CharField(max_length=10)

    def __str__(self):
        return self.account_number, self.bank


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        TRANSFER = 'Transfer'
        WITHDRAWAL = 'Withdrawal'
        DEPOSIT = 'Deposit'
        AIRTIME = 'Airtime'
        UTILITY_BILL = 'Utility_bill'

    class TransactionStatus(models.TextChoices):
        PENDING = 'Pending'
        SUCCESS = 'SUCCESS'
        FAILED = 'Failed'

    beneficiary = models.ForeignKey('WalletUser', on_delete=models.PROTECT, related_name='sender')
    transaction_type = models.CharField(choices=TransactionType.choices, max_length=15, default=None)
    transaction_status = models.CharField(choices=TransactionStatus.choices, max_length=15, default=None)
    transaction_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return '%s %s %s' % (self.transaction_type, self.transaction_status, self.amount)


# class Service(Enum):
#     pass


class Saving(models.Model):
    class SavingPlan(models.TextChoices):
        WEEKLY = 'Weekly'
        BIWEEKLY = 'Biweekly'
        MONTHLY = 'Monthly'
        QUARTERLY = 'Quarterly'

    title = models.CharField(max_length=150)
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    saving_plan = models.CharField(choices=SavingPlan.choices, default=None, max_length=15)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True, blank=True, null=True)
    balance = models.DecimalField(decimal_places=2, max_digits=15, default=0.0)

    def __str__(self):
        return self.title


class DebitCard(models.Model):
    account = models.ForeignKey('Account', on_delete=CASCADE, related_name='card_holder')
    card_number = models.CharField(max_length=19)
    expiry_date = models.DateTimeField()
    cvv = models.CharField(max_length=3)
    card_holder_name = models.CharField(max_length=50)

    def __str__(self):
        return self.card_holder_name, self.card_number


class Wallet(models.Model):
    balance = models.DecimalField(max_digits=25, decimal_places=2, default=0.0)
    wallet_user = models.ForeignKey('WalletUser', on_delete=CASCADE, related_name='user')
    saving = models.ForeignKey(Saving, on_delete=models.SET_NULL, related_name='savings',
                               default=None, null=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, related_name='transactions',
                                    default=None, null=True)
    card = models.ForeignKey(DebitCard, on_delete=models.PROTECT, related_name='cards', default=None)

    def __str__(self):
        return '%s %s' % (self.wallet_user_id, self.balance)


class NextOfKin(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    phone_number = models.CharField(max_length=13)
    relationship = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    address = models.TextField()

    def __str__(self):
        return self.first_name, self.last_name


class WalletUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    next_of_kin = models.ForeignKey(NextOfKin, blank=True, null=True,
                                    on_delete=models.SET_NULL, related_name="next_of_kin")
    BVN = models.CharField(max_length=11)
    NIN = models.CharField(max_length=10)
    display_photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()
