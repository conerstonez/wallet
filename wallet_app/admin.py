from django.contrib import admin
from wallet_app.models import *


@admin.register(WalletUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'updated_at', 'display_photo']
    # list_filter = ['title']
    # list_per_page = 10
    # list_editable = []
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['beneficiary', 'transaction_type', 'transaction_status', 'transaction_time', 'amount']


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['wallet_number', 'balance']


@admin.register(DebitCard)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(Saving)
class SavingAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(NextOfKin)
class NextOfKinAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone_number', 'email', 'address']
