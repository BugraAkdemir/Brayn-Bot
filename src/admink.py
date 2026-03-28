import discord
from discord.ext import commands

class ADMİN_KOMUTLARI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command()
    async def BUGRA(self, ctx):
        await ctx.send("MERHABA!")
        
        
    
def setup(bot):
    bot.add_cog(ADMİN_KOMUTLARI(bot))