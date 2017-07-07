import discord
from discord.ext import commands
from google.cloud import translate

class Translate:
    def __init__(self,bot):
        self.bot = bot
        
        #alias allows (for example) !template or !myTemplate as the command. pass_context allows you to check message author so you can @mention them.
    
    @commands.command(
        name='translate',
        aliases=['translator','translation'],
        description='A Translator made using Google Translation\'s API',
        brief='Simple Translator',
        pass_context = True
    )

    async def translate(self,ctx,*,message):
        full = message.split(" ",1)
        targ = full[0]
        tex = ''
        for index in range(0,len(full)):
            if index != 0:
                tex += full[index]
        msg = self.translate_text(targ,tex)
        if(len(msg) <= 50):
            await self.bot.say(msg)
        else:
            await self.bot.say("Please keep the message shorter than 50 characters.")
    
    def translate_text(self,target, text):
        translate_client = translate.Client()
        
        ##if isinstance(text, six.binary_type):
          ##  text = text.decode('utf-8')

        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        result = translate_client.translate(
            text, target_language=target)
        return('Translation: {}'.format(result['translatedText']))

def setup(bot):
    bot.add_cog(Translate(bot))
#The last thing to do is to go to the DiscordBot.py and add commands.<insertclassname>
