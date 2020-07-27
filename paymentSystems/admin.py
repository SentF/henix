import sys

from django.contrib import admin

# Register your models here.
from paymentSystems.bitgo import Bitgo


if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
    Bitgo().get_wallet()
