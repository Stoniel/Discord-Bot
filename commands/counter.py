import discord
from discord.ext import commands

class Counter:
    def __init__(self,bot):
        self.bot = bot
        self.count = 0
    @commands.command(
        name='count',
        aliases=['counter'],
        description='Simple Counter',
        brief='Example of Storing Info',
        pass_context = True
    )
    async def counter(self,ctx):
        self.count += 1
        msg = '<@' + str(ctx.message.author.id) + '> ' +  str(self.count)
        await self.bot.say(msg)
        
def setup(bot):
    bot.add_cog(Counter(bot))
