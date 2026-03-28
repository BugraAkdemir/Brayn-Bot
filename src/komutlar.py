import discord
from discord.ext import commands

class Oyunlar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command()
    async def merhaba(self, ctx):
        await ctx.send("ALL SDSLDLS")
        
        
    
def setup(bot):
    bot.add_cog(Oyunlar(bot))