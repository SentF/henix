from django.db import models

from localusers.models import LocalUser


class Game(models.Model):
    name = models.CharField('Name', max_length=20)
    image = models.ImageField("Image", upload_to="game_images", blank=True, null=True)

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
    price = models.FloatField('Price')

    oc_support = models.CharField('OC Support', max_length=64)

    def __str__(self):
        return f"{self.game.name} - {self.name}"


class CheatFunction(models.Model):
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.CASCADE)

    name = models.CharField('Name', max_length=64)
    description = models.TextField('Description', blank=True, default="The best function")

    def __str__(self):
        return f"{self.cheat.name} - {self.name}"


class Key(models.Model):
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.CASCADE)

    key = models.CharField('Key', max_length=64)
    is_sold = models.BooleanField('Is sold', blank=True, default=False)

    def __str__(self):
        return f"{self.cheat.name} - {self.id}"


class Detection(models.Model):
    title = models.CharField('Title', max_length=24)
    last_hit = models.DateTimeField('Last hit', null=True, blank=True)
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cheat.name} - {self.last_hit}"


class Purchase(models.Model):
    cheat = models.ForeignKey("Cheat", verbose_name="Cheat", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(LocalUser, verbose_name="User", on_delete=models.SET_NULL, null=True)

    date = models.DateTimeField('Date')
    PAYMENT_CHOICES = (
        ("Card", "Card"),
        ("Bitcoin", "Bitcoin"),
        ("PayPal", "PayPal")
    )
    payment = models.CharField('Payment method', choices=PAYMENT_CHOICES, max_length=16)
    payment_id = models.CharField('Payment id', max_length=64)
    STATUS_CHOICES = (
        ("Unpaid", "Unpaid"),
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    )
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=24)
    key = models.CharField('Key', max_length=32, blank=True)

    def get_color(self):
        choices = {
            'Unpaid': 'red_text',
            'Pending': 'yellow_text',
            'Paid': 'positive_text'
        }
        return choices[self.status]

    def get_tooltip(self):
        choices = {
            'Unpaid': 'Not paid yet. Please paid to get this.',
            'Pending': 'Payment pending.',
            'Paid': 'You can get and activate key'
        }
        return choices[self.status]

    def __str__(self):
        return f"{self.user.username} - {self.cheat.name}"


class Announcement(models.Model):
    created_at = models.DateTimeField('Creation date', auto_now_add=True, blank=True)
    title = models.CharField('Title', max_length=20)
    text = models.TextField('Text')

    def __str__(self):
        return f"{self.title}"
