import discord
from discord.ext import commands

class RockPaperScissors:
    def __init__(self,bot):
        self.bot = bot
        self.choices = ['']
        self.ids = [0]
    
    @commands.group(
        description='Rock Paper Scissors',
        brief='Rock Paper Scissors!',
        pass_context = True
    )

    async def rps(self,ctx):
        msg = 'Type <!rps Choice> '
        await self.bot.say(msg)
        
    @rps.command(
        name='rock',
        description = "Choice Rock",
        brief = 'Choose Rock',
        pass_context = True
    )

    async def rock(self,ctx):
        if(self.choices[0] == ''):
            self.choices[0] = 'rock'
        else:
            self.choices.append('rock')
        
    @rps.command(
        name='paper',
        description = "Choice Paper",
        brief = 'Choose Paper',
        pass_context = True
    )
    async def paper(self,ctx):
        if(self.choices[0] == ''):
            self.choices[0] = 'paper'
        else:
            self.choices.append('paper')
    
def setup(bot):
    bot.add_cog(RockPaperScissors(bot))
