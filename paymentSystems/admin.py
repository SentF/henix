from django.contrib import admin

# Register your models here.
from paymentSystems.bitgo import Bitgo

Bitgo().get_wallet()
