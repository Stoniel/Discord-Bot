import discord
from discord.ext import commands

class Raids:
    def __init__(self,bot):
        self.bot = bot
        
        #alias allows (for example) !template or !myTemplate as the command. pass_context allows you to check message author so you can @mention them.
    
    @commands.command(
        name='raids',
        aliases=['xeric','raid'],
        description='Full Raids Set-Up Pre Arma/Bandos/BP',
        brief='Raids Set-Up',
        pass_context = True
    )

    async def raids(self,ctx):
        msg = 'https://gyazo.com/3bbeed8086082e9ff9b8e652f1f9f091'
        await self.bot.say(msg)
    
def setup(bot):
    bot.add_cog(Raids(bot))
#The last thing to do is to go to the DiscordBot.py and add commands.<insertclassname>
