#@author: Stone Daniel July 2017
import discord
from discord.ext import commands
from google.cloud import translate

class Translate:
    def __init__(self,bot):
        self.bot = bot
        
    
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
        if(len(msg) <= 100):
            await self.bot.say(msg)
        else:
            await self.bot.say("Please keep the message shorter than 100 characters.")
    
    def translate_text(self,target, text):
        translate_client = translate.Client()
        result = translate_client.translate(
            text, target_language=target)
        return('Translation: {}'.format(result['translatedText']))

def setup(bot):
    bot.add_cog(Translate(bot))
