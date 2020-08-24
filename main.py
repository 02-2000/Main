import asyncio
import json
import sqlite3
import discord
from discord.ext import commands

TOKEN = 'dein token hier'

bot = commands.Bot(command_prefix="d.")

bot.remove_command('help')
########################################################################################################################

extensions = ['deinpath zb cogs.test']

@bot.event
async def on_ready():
    print('--------------------------------------')
    print('Bot is ready.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------------------------')
    await status_task()


########################################################################################################################
async def status_task():
    await bot.change_presence(activity=discord.Game('droidebot.xyz'), status=discord.Status.online)
#################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} was not loaded. [{}]'.format(extension, error))

bot.run(TOKEN)
