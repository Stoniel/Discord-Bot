import discord
from discord.ext import commands
from random import randint

class Dice:
    def __init__(self,bot):
        self.bot = bot
        
        
        #alias allows (for example) !template or !myTemplate as the command. pass_context allows you to check message author so you can @mention them.
    
    @commands.command(
        name='dice',
        aliases=['mydice'],
        description='Rolling a single die',
        brief='Ryan\'s template',
        pass_context = True
    )

    async def Dice(self,ctx):
        msg = randint(1,6)
        await self.bot.say("{} Your number is \n".format(ctx.message.author.mention) +  str(msg))
        await self.bot.say("You lose")
        await self.bot.say("Also, you are ugly")
        
def setup(bot):
    bot.add_cog(Dice(bot))
#The last thing to do is to go to the DiscordBot.py and add commands.<insertclassname>
