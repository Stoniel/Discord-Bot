import discord
from discord.ext import commands

class UnixComs:
    def __init__(self,bot):
        self.bot = bot
        
        #alias allows (for example) !template or !myTemplate as the command. pass_context allows you to check message author so you can @mention them.
    
    @commands.command(
        name='linux',
        aliases=['unix'],
        description='A short list of useful Unix Commands for those new to terminals',
        brief='Short List of Unix Commands',
        pass_context = True
    )

    async def unix(self,ctx):
        msg = ('``` cd <path>: Change Directory to Specific Path, no path given will return you to your home directory \n\n'
        'mkdir <desiredName> : Make a directory\n\n'
        'pwd: Present Working Directory, the path to your current location\n\n'
        'rm (-rf) <toRemove>: Removes file given. If you want to ignore warnings add -f, if you want to delete a directory type -r\n\n'
        'mv <oldFileName> <newFileName>: Move file, can be moved to a directory, or be used to rename a file\n\n'
        'cp <originalFileName> <targetName>: Creates a copy of the file\n\n'
        'clear: Clears the screen ```')
        await self.bot.say(msg)
    
def setup(bot):
    bot.add_cog(UnixComs(bot))
#The last thing to do is to go to the DiscordBot.py and add commands.<insertclassname>
