import sys

from django.contrib import admin

# Register your models here.
from paymentSystems.bitgo import Bitgo, OtherBitgo

if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
    try:
        Bitgo().get_wallet()
    except OtherBitgo as err:
        print(err)
