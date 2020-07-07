from allauth.socialaccount.models import SocialAccount
from django import template

from main.models import Cheat

register = template.Library()


@register.filter(name='last_detect')
def last_detect(value):
    return "None" if Cheat.objects.get(id=value).detection_set.last() is None\
        else Cheat.objects.get(id=value).detection_set.last().hit_at.date()


@register.filter(name='functions')
def functions(value, split):
    funcs = Cheat.objects.get(id=value).cheatfunction_set.all()
    half = len(funcs) // 2
    if split == 0:
        return funcs[:half]
    else:
        return funcs[half:]


@register.filter(name='quantity')
def quantity(value):
    return Cheat.objects.get(id=value).key_set.filter(is_sold=False).count()
