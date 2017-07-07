import discord
from discord.ext import commands
import requests
import json

class Blackjack:
    def __init__(self,bot):
        self.bot = bot
        self.ids = []
        self.deck_id = 1
        self.hands[]
        self.handCodes[]
        #alias allows (for example) !template or !myTemplate as the command. pass_context allows you to check message author so you can @mention them.
    
    @commands.group(
        name='blackjack',
        aliases=['Blackjack','bj'],
        description='A simple BlackJack program',
        brief='A game of 21.',
        pass_context = True,
        invoke_without_command = True
    )

    async def blackjack(self,ctx,*,message):
        new_player = ctx.author.id
        msg = ''
        for i in self.ids:
            if(i == new_player): 
                await self.bot.say("You are already in the queue. \"!blackjack start\"")
                return
            else:
                msg += "<@" + str(i) + "> "
        await self.bot.say("The current queue includes " + msg)
    

    @blackjack.command(
        name = "start",
        description = "Start Game, which takes everyone in the queue and gives them each two starting cards.",
        brief = "Start Game!",
)
    async def start(self):
        r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        json_data = r.json()
        if json_data["success"] == 'true':
            self.deck_id = json_data["deck_id"]
        else:
            return
        for index,i in self.ids:
            r = requests.get('https://deckofcardsapi.com/api/deck/' + self.deck_id + '/draw/?count=2')
            json_data = r.json()
            #Need to learn more about JSON here
            cur_hand = [(json_data["cards"]["value"] + " of " + json_data["cards"]["suit"],(json_data["cards"]["value"] + " of " + json_data["cards"]["suit"] )]
            cur_codes = []
            self.hands.append(cur_hand)
        
)



def setup(bot):
    bot.add_cog(Blackjack(bot))
#The last thing to do is to go to the DiscordBot.py and add commands.<insertclassname>
