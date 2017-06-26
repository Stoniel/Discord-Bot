import discord
from discord.ext import commands

class Template:
    def __init__(self,bot):
        self.bot = bot
        self.var = 'This is just some var you want to make. Dont need String/int/etc its automatic'
        
        #alias allows (for example) !template or !myTemplate as the command. pass_context allows you to check message author so you can @mention them.
    
    @commands.command(
        name='template',
        aliases=['myTemplate','otherstuff'],
        description='Template Command',
        brief='Ryas\'s template',
        pass_context = True
    )

    async def template(self,ctx,*,message):
        msg = message
        await self.bot.say(msg)
    
def setup(bot):
    bot.add_cog(Template(bot))
#The last thing to do is to go to the DiscordBot.py and add commands.<insertclassname>
