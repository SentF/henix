from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from main.models import Game, Cheat, Purchase, CheatFunction, Key, Detection, Announcement, CheatImage, CheatVideo, \
    Price


# region filters
class UserFilter(admin.SimpleListFilter):
    title = _('user')
    parameter_name = 'user'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        return set((pur.user.username, pur.user.username) for pur in qs)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(user__username=self.value())


# endregion

# region register
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class CheatImageInline(admin.StackedInline):
    min_num = 0
    extra = 0
    can_delete = True
    model = CheatImage


class CheatVideoInline(admin.StackedInline):
    min_num = 0
    extra = 0
    can_delete = True
    model = CheatVideo


class CheatKeyInline(admin.StackedInline):
    min_num = 0
    extra = 0
    can_delete = True
    model = Key

class CheatPriceInline(admin.StackedInline):
    min_num = 0
    extra = 0
    can_delete = True
    model = Price


class CheatFunctionInline(admin.StackedInline):
    min_num = 0
    extra = 0
    can_delete = True
    model = CheatFunction


@admin.register(Cheat)
class CheatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'game_link', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    list_filter = ('game',)
    inlines = (CheatKeyInline, CheatPriceInline, CheatImageInline, CheatVideoInline, CheatFunctionInline)

    def game_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:main_game_change", args=(obj.game.id,)),
            obj.game.name
        ))

    game_link.short_description = 'game'


@admin.register(Detection)
class DetectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cheat_link', 'last_hit')
    list_display_links = ('id', 'title')

    def cheat_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:main_cheat_change", args=(obj.cheat.id,)),
            obj.cheat.name
        ))

    cheat_link.short_description = 'cheat'


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_id', 'user_link', 'cheat_link', 'payment', 'status', 'date')
    list_display_links = ('id', 'payment_id')
    list_filter = ('payment', 'status', UserFilter)

    def user_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:localusers_localuser_change", args=(obj.user.id,)),
            obj.user.username
        ))

    user_link.short_description = 'user'
    user_link.admin_order_field = 'user'

    def cheat_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:main_cheat_change", args=(obj.cheat.id,)),
            obj.cheat.name
        ))

    cheat_link.short_description = 'cheat'


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
# endregion
