import json

from allauth.socialaccount.models import SocialAccount
from django import template

register = template.Library()


@register.filter(name='get_avatar')
def get_avatar(value):
    data = SocialAccount.objects.get(user_id=value).extra_data
    return f'https://cdn.discordapp.com/avatars/{data["id"]}/{data["avatar"]}'
