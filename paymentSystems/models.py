from django.db import models
from main.models import *


# Create your models here.
class BitcoinPayment(models.Model):
    address = models.CharField("Address", max_length=64)


class Payment(models.Model):
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)

    bitcoin = models.OneToOneField(BitcoinPayment, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def cost(self):
        return sum([key.price for key in self.purchase.key_set.all()])
