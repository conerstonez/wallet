import random

# from wallet_app.models import Wallet


def create_new_ref_number():
    # unique_ref = 0
    # not_unique = True
    # while not_unique:
    return random.randint(1000000000, 9999999999)
    #     if not Wallet.objects.filter(wallet_number=unique_ref):
    #         not_unique = False
    # return str(unique_ref)
