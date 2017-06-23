import discord
from time import sleep
from discord.ext import commands

class Timer:
    def __init__(self,bot):
        self.bot = bot

    @commands.command(
        pass_context = True,
        name = "timer",
        aliases = ['time'],
        description = "Countdown Timer",
        brief = 'This is a timer'
    )
    async def timer(self,ctx, max = 3):
        if not isinstance(max,(int , float)):
            await self.bot.say("{} Timer must be a number.".format(ctx.message.author.mention))
        elif 1<= max <= 30:
            for i in range(max,0,-1):
                await self.bot.say(i)
                sleep(.85)
            await self.bot.say("GO!")
        else:
            await self.bot.say("Timer number must be less than 30.")
def setup(bot):
    bot.add_cog(Timer(bot))
