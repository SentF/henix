import asyncio
import os
import threading
import discord
from allauth.socialaccount.models import SocialAccount
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

from main.models import Game, Purchase, Key


def start():
    thread = threading.Timer(0, ds)
    thread.daemon = True
    thread.start()


def ds():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            game = await sync_to_async(lambda: Game.objects.all()[0], thread_sensitive=True)()
            await message.channel.send(game.name)

    @client.event
    async def on_member_join(member):
        keys = await on_member_join_db(member)
        for key in keys:
            print(1)
            role = await member.guild.roles.get_role(key.cheat.ds_role_id)
            print(2)
            print(str(key.cheat.ds_role_id))
            if role != None: await member.add_roles(role)


    @client.event
    async def on_error(event, *args, **kwargs):
        client.run(os.environ.get('DS_BOT_TOKEN'))

    client.run(os.environ.get('DS_BOT_TOKEN'))


async def on_member_join_db(member):
    allAccounts = await sync_to_async(lambda: SocialAccount.objects.all(), thread_sensitive=True)()
    for acc in allAccounts:
        if acc.extra_data['id'] == str(member.id):
            account_id = acc.extra_data['id']
            purchases = await database_sync_to_async(lambda: Purchase.objects.all(), thread_sensitive=True)()
            purchases = list(filter(lambda p: str(p.user.socialaccount_set.all()[0].uid) == account_id, purchases))
            keys = [await database_sync_to_async(lambda: Key.objects.all(), thread_sensitive=True)() for purchase in purchases]
            return keys
        break
    return []