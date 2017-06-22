import discord
from discord.ext import commands

class RockPaperScissors:
    def __init__(self,bot):
        self.bot = bot
        self.choices = ['']
        self.ids = [0]
    
    async def who_wins(self):
        if len(self.choices) == 1:
            return
        else:
            if self.choices[0] == 'rock' and self.choices[1]  == 'paper':
                 msg = '<@' + str(self.ids[1]) + '> You Win!'
            elif self.choices[0] == 'paper' and self.choices[1] == 'scissors':
                msg = '<@' + str(self.ids[1]) + '> You Win!'
            elif self.choices[0] == 'scissors' and self.choices[1] == 'rock':
                msg = '<@' + str(self.ids[1]) + '> You Win!'
            if self.choices[1] == 'rock' and self.choices[0]  == 'paper':
                msg = '<@' + str(self.ids[0]) + '> You Win!'
            elif self.choices[1] == 'paper' and self.choices[0] == 'scissors':
                msg = '<@' + str(self.ids[0]) + '> You Win!'
            elif self.choices[1] == 'scissors' and self.choices[0] == 'rock':
                msg = '<@' + str(self.ids[0]) + '> You Win!'
            elif self.choices[0] == self.choices[1]:
                msg = "Tie Game!"
            await self.bot.say(msg)
            self.ids = [0]
            self.choices = ['']


    @commands.group(
        name = 'rps',
        description='Rock Paper Scissors',
        brief='Rock Paper Scissors!',
        pass_context = True,
        invoke_without_command = True
    )

    async def rps(self,ctx):
            #if len(message) <= 1:
        await self.bot.say("Say \"!rps <Rock/Paper/Scissors> \" to make your choice")
                
    @rps.command(
        name='rock',
        description = "Choice Rock",
        brief = 'Choose Rock',
        pass_context = True
    )

    async def rock(self,ctx):
        if(self.choices[0] == ''):
            self.choices[0] = 'rock'
            self.ids[0] = ctx.message.author.id
        else:
            self.choices.append('rock')
            self.ids.append(ctx.message.author.id)
            await self.who_wins()

    @rps.command(
        name='paper',
        description = "Choice Paper",
        brief = 'Choose Paper',
        pass_context = True
    )
    async def paper(self,ctx):
        if(self.choices[0] == ''):
            self.choices[0] = 'paper'
            self.ids[0] = ctx.message.author.id
        else:
            self.choices.append('paper')
            self.ids.append(ctx.message.author.id)
            await self.who_wins()

    @rps.command(
        name='scissors',
        description = "Choice Scissors",
        brief = 'Choose Scissors',
        pass_context = True
    )
    async def scissors(self,ctx):
        if(self.choices[0] == ''):
            self.choices[0] = 'scissors'
            self.ids[0] = ctx.message.author.id
        else:
            self.choices.append('scissors')
            self.ids.append(ctx.message.author.id)
            await self.who_wins()

def setup(bot):
    bot.add_cog(RockPaperScissors(bot))
