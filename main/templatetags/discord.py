from allauth.socialaccount.models import SocialAccount
from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.templatetags.static import static

register = template.Library()


@register.filter(name='get_avatar')
def get_avatar(value):
    try:
        data = SocialAccount.objects.get(user_id=value).extra_data
        return f'https://cdn.discordapp.com/avatars/{data["id"]}/{data["avatar"]}'
    except ObjectDoesNotExist:
        return static('images/profile.png')

