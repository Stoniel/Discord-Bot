import discord
from discord.ext import commands

class Counter:
    def __init__(self,bot):
        self.bot = bot
        self.count = [0]
        self.ids = [0]
    @commands.command(
        name='count',
        aliases=['counter'],
        description='Simple Counter',
        brief='Example of Storing Info',
        pass_context = True
    )
    async def counter(self,ctx):
        for i,item in enumerate(self.ids):
            if(ctx.message.author.id == item):
                self.count[i] += 1
                msg = '<@' + str(ctx.message.author.id) + '> ' +  str(self.count[i])
                break
            elif(i == len(self.ids)-1):
                self.ids.append(ctx.message.author.id)
                self.count.append(0)
                msg = '<@' + str(ctx.message.author.id) + '> ' +  str(self.count[i])
        await self.bot.say(msg + ' Index of ID# ' + str(i))
        
def setup(bot):
    bot.add_cog(Counter(bot))
