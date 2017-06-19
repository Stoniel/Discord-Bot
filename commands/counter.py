import discord
from discord.ext import commands

class Counter:
    def __init__(self,bot):
        self.bot = bot
        self.count = 0
 
    @commands.command(
        name='count',
        aliases=['counter'],
        description='whatever',
        brief='hello'
    )
    async def counter(self):
        self.count += 1
        await self.bot.say(':smile: ' + str(self.count))
        
def setup(bot):
    bot.add_cog(Counter(bot))
