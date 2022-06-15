import discord
from discord.ext import commands

class ReadyCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('Blade Idle'))
        print('Bot is now running')

    @commands.command()
    async def echo(self, ctx):
        await ctx.send(ctx.message.content[5:])
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(ReadyCog(bot))