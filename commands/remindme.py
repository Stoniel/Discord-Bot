import discord
from time import sleep
from discord.ext import commands

class RemindMe:
    def __init__(self,bot):
        self.bot = bot

    @commands.command(
        pass_context = True,
        name = "remindme",
        aliases = ['reminder','remind'],
        description = "Reminder in Minutes",
        brief = 'Reminder'
    )
    async def timer(self,ctx, max = 10):
        if not isinstance(max,(int , float)):
            await self.bot.say("{} Reminder must be a number.".format(ctx.message.author.mention))
        elif 1<= max <= 60:
            await self.bot.say(('{} Timer set for ' + str(max) + 'minutes').format(ctx.message.author.mention))  
            for i in range(max,0,-1):
                sleep(max*60)
            await self.bot.say("{} Your Timer is up!".format(ctx.message.author.mention))
        else:
            await self.bot.say("Timer number must be less than 30.")
def setup(bot):
    bot.add_cog(RemindMe(bot))
