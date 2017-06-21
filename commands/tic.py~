import discord
from discord.ext import commands

class Tic:
    def __init__(self,bot):
        self.bot = bot
        self.array = [['_','_','_'],['_','_','_'],['_','_','_']]
        self.idList[0,0]
        
        #alias allows (for example) !template or !myTemplate as the command. pass_context allows you to check message author so you can @mention them.
    
    @commands.command(
        name='tic',
        aliases=['tac','toe'],
        description='Tic Tac Toe game',
        brief='Simple Tic Tac Toe game',
        pass_context = True
    )

    async def tic(self,ctx):
        output = ''
        for i in self.array:
            for j in range(0, len(i)):
                output += i[j]
                if j != len(i) - 1:
                    output += '|'
                    output += '\n'
        await self.bot.say(output)
    
    @commands.command(
        name='up',
        aliases=[],
        description='Tic Tac Toe game',
        brief='Simple Tic Tac Toe game'
   )
    async def up(self):
        if self.count%2 == 0:
            self.array[0][1] = 'X'
        else:
            self.array[0][1] = 'O'
        self.print_array()
    
    @commands.command(
        name='down',
        aliases=[],
        description='Tic Tac Toe game',
        brief='Down'  
 )
   async def down(self):
        if self.count % 2 == 0:
            self.array[2][1] = 'X'
        else:
            self.array[2][1] = 'O'
        self.print_array()
    
    @command.command(
        name='left',
        aliases=[],
        description='Tic Tac Toe game',
        brief='Simple Tic Tac Toe game'   
    )
    def left(self):
        if self.count % 2 == 0:
            self.array[1][0] = 'X'
        else:
            self.array[1][0] = 'O'
        self.print_array()
    
    @command.command(
        name='up',
        aliases=[],
        description='Tic Tac Toe game',
        brief='Simple Tic Tac Toe game'   
    )
    def right(self):
        if self.count % 2 == 0:
            self.array[1][2] = 'X'
        else:
            self.array[1][2] = 'O'
        self.print_array()
    
def setup(bot):
    bot.add_cog(Tic(bot))
#The last thing to do is to go to the DiscordBot.py and add commands.<insertclassname>
