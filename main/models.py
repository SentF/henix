import os
import requests
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.db import models
from localusers.models import LocalUser


class DSServer(models.Model):
    name = models.CharField('Name', max_length=16, blank=True, null=True)
    ds_server_id = models.IntegerField('Discord server ID', blank=True, null=True)

    is_common = models.BooleanField('Is common', blank=True, default=False)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.ds_server_id

    def save(self, *args, **kwargs):
        if self.is_common:
            for user in SocialAccount.objects.all():
                r = requests.put(
                    f'https://discord.com/api/guilds/{self.ds_server_id}/members/{user.extra_data["id"]}',
                    json={'access_token': SocialToken.objects.get(account__user=user.user).token},
                    headers={f'Authorization': f'Bot {os.environ.get("DS_BOT_TOKEN")}',
                             'Content-Type': 'application/json'}
                )
        super().save(*args, **kwargs)


class Game(models.Model):
    name = models.CharField('Name', max_length=20)
    description = models.TextField('Description', blank=True, default="")
    image = models.ImageField("Image", upload_to="game_images", blank=False, null=True)

    def __str__(self):
        return self.name


class Cheat(models.Model):
    game = models.ForeignKey("Game", verbose_name="Game", on_delete=models.SET_NULL, null=True)
    name = models.CharField('Name', max_length=20)
    mini_description = models.CharField('Mini description', max_length=64, blank=True, null=True)
    image = models.ImageField("Image", upload_to="cheat_images", blank=True, null=True)

    created_at = models.DateTimeField('Creation date', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('Update date', auto_now_add=True, blank=True)
    STATUS_CHOICES = (
        ("Detected", "Detected"),
        ("Undetected", "Undetected"),
    )
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=24)
    is_selected = models.BooleanField('Is selected', default=False)

    oc_support = models.CharField('OC Support', max_length=64, blank=True)
    hardware_support = models.CharField('Hardware Support', max_length=64, blank=True)

    ds_server = models.ForeignKey(DSServer, verbose_name="Discord server", on_delete=models.SET_NULL, null=True,
                                  blank=True)
    ds_role_id = models.IntegerField('Discord role ID', blank=True, null=True)

    def __str__(self):
        return f"{self.game.name} - {self.name}"


class CheatFunction(models.Model):
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.CASCADE)

    name = models.CharField('Name', max_length=64)
    description = models.TextField('Description', blank=True, default="The best function")

    def __str__(self):
        return f"{self.cheat.name} - {self.name}"


class CheatImage(models.Model):
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.CASCADE)
    image = models.ImageField("Image", upload_to="cheat_images")


class CheatVideo(models.Model):
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.CASCADE)
    video = models.CharField("Video id from youtube", max_length=16, default="tgbNymZ7vqY")


class Purchase(models.Model):
    user = models.ForeignKey(LocalUser, verbose_name="User", on_delete=models.SET_NULL, null=True)

    date = models.DateTimeField('Date')
    PAYMENT_CHOICES = (
        ("Card", "Card"),
        ("Bitcoin", "Bitcoin"),
        ("PayPal", "PayPal")
    )
    payment_method = models.CharField('Payment method', choices=PAYMENT_CHOICES, max_length=16)
    payment_id = models.CharField('Payment id', max_length=64)
    STATUS_CHOICES = (
        ("Unpaid", "Unpaid"),
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    )
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=24)

    def get_color(self):
        choices = {
            'Unpaid': 'red_text',
            'Pending': 'yellow_text',
            'Paid': 'positive_text'
        }
        return choices[self.status]

    def get_tooltip(self):
        choices = {
            'Unpaid': 'Canceled',
            'Pending': 'Not paid yet. Please paid to get this.',
            'Paid': 'You can get and activate key'
        }
        return choices[self.status]

    def __str__(self):
        return f"{self.user.username} - {self.date.day}.{self.date.month}.{self.date.year}"

    def save(self, *args, **kwargs):
        if self.key_set.count() != 0:
            if self.key_set.all()[0].cheat.ds_server is not None:
                r = requests.put(
                    f'https://discord.com/api/guilds/{self.key_set.all()[0].cheat.ds_server.ds_server_id}/members/{SocialAccount.objects.get(user=self.user).extra_data["id"]}',
                    json={'access_token': SocialToken.objects.get(account__user=self.user).token},
                    headers={f'Authorization': f'Bot {os.environ.get("DS_BOT_TOKEN")}',
                             'Content-Type': 'application/json'})
        super().save(*args, **kwargs)


class PurchaseDSLink(models.Model):
    purchase = models.ForeignKey("Purchase", verbose_name="Purchase", on_delete=models.CASCADE)
    ds_link = models.CharField("Server link", max_length=32)  # or 25


class Key(models.Model):
    purchase = models.ForeignKey("Purchase", verbose_name="Purchase", on_delete=models.CASCADE, blank=True, null=True)
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.CASCADE)

    key = models.CharField('Key', max_length=64)
    duration = models.IntegerField('Duration in days', default='30')

    def __str__(self):
        return f"{self.cheat.name} - {self.id}"

    @property
    def price(self):
        return self.cheat.price_set.get(duration=self.duration).price


class Price(models.Model):
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.CASCADE)

    price = models.FloatField('Price')
    duration = models.IntegerField('Duration in days', default='30')

    def __str__(self):
        return f"{self.cheat.name} - {self.duration}"


class Detection(models.Model):
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.CASCADE)

    title = models.CharField('Title', max_length=24)
    hit_at = models.DateTimeField('Hit at')

    def __str__(self):
        return f"{self.cheat.name} - {self.hit_at}"


class Announcement(models.Model):
    created_at = models.DateTimeField('Creation date', auto_now_add=True, blank=True)
    title = models.CharField('Title', max_length=20)
    text = models.TextField('Text')

    button_text = models.CharField('Button text', max_length=32, blank=True, default='')
    button_link = models.CharField('Button link', max_length=128, blank=True, default='')

    def __str__(self):
        return f"{self.title}"
