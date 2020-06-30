from django.db import models

from localusers.models import LocalUser


class Game(models.Model):
    name = models.CharField('Name', max_length=20)
    image = models.ImageField("Image", upload_to="game_images", blank=True, null=True)


class Cheat(models.Model):
    name = models.CharField('Name', max_length=20)
    image = models.ImageField("Image", upload_to="cheat_images", blank=True, null=True)

    created_at = models.DateTimeField('Creation date', auto_now_add=True, blank=True)
    last_detect_at = models.DateTimeField('Detection date', null=True, blank=True)
    updated_at = models.DateTimeField('Update date', auto_now_add=True, blank=True)

    game = models.ForeignKey("Game", verbose_name="Game", on_delete=models.SET_NULL, null=True)


class Purchase(models.Model):
    date = models.DateTimeField('Date')
    payment = models.CharField('Payment method', max_length=16)
    payment_id = models.CharField('Payment method', max_length=64)
    status = models.CharField('Status', max_length=16)
    key = models.CharField('Key', max_length=32)

    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(LocalUser, verbose_name="User", on_delete=models.CASCADE)

# TODO announcements and detection history
