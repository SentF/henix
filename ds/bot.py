import os
import threading
from functools import partial

import discord
from discord.ext import commands
from allauth.socialaccount.models import SocialAccount

from main.models import Game, Key

bot = commands.Bot("_")

def start():
    thread = threading.Timer(0, ds)
    thread.daemon = True
    thread.start()

def ds():
    @bot.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(bot))


    @commands.command()
    async def hello(ctx):
        game = (await bot.loop.run_in_executor(None, Game.objects.all))[0]
        await ctx.send(game.name)


    @bot.event
    async def on_member_join(member):
        allAccounts = await bot.loop.run_in_executor(None, SocialAccount.objects.all)
        for acc in allAccounts:
            if acc.extra_data['id'] == str(member.id):
                account_id = acc.extra_data['id']
                purchases = await bot.loop.run_in_executor(None, partial(Key.objects.filter, user__id=account_id))
                keys = [await bot.loop.run_in_executor(None, partial(Key.objects.filter, purchase__id=purchase.id)) for
                        purchase in purchases]
        for key in keys:
            role = discord.utils.get(member.guild.roles, id=key.cheat.ds_role_id)
            print(str(key.cheat.ds_role_id))
            await member.add_roles(role)
            break


    bot.run(os.environ.get('DS_BOT_TOKEN'))