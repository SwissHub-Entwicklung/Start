import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def swisshub(ctx):
    await ctx.send('Starting...')

bot.run('token')
