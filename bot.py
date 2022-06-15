from discord.ext import commands
import os

discord_token = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix="+")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for cog in ['ready', 'notify']:
    bot.load_extension(f'cogs.{cog}')

bot.run(discord_token)