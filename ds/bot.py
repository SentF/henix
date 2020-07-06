import asyncio
import os
import threading
import discord
from channels.db import database_sync_to_async

from main.models import Game


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
            game = await database_sync_to_async(lambda: Game.objects.all()[0])()
            await message.channel.send(game.name)

    client.run(os.environ.get('DS_BOT_TOKEN'))
