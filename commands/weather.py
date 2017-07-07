import discord
from discord.ext import commands
import json
import requests
import secrets

class Weather:
    def __init__(self,bot):
        self.bot = bot
        
        #alias allows (for example) !template or !myTemplate as the command. pass_context allows you to check message author so you can @mention them.
    
    @commands.group(
        name='weather',
        aliases=['forecast'],
        description='Provides a forecast for a desired location',
        brief='Weather',
        pass_context = True,
        run_without_commands = True
    )

    async def weather(self,ctx,*,message):
        #locs = {}
        #with open('locations.json','r') as f:
        #    locs = json.load(f)
        #lat = locs['athens,ga'][0]
        #longitude = locs['athens,ga'][1]
        #loc = "Athens,GA"
        geocode = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + message + '&key=' + secrets.geocode_API)
        loc = geocode.json()['results'][0]['address_components'][0]['long_name']
        lat = geocode.json()['results'][0]['geometry']['location']['lat']
        longitude = geocode.json()['results'][0]['geometry']['location']['lng']
        coords = str(lat) + ',' + str(longitude)
        response = requests.get('https://api.darksky.net/forecast/' + secrets.weather_key + "/" + coords)
        msg = "The weather in " + loc  + " is " + response.json()["currently"]["summary"] + ". It is currently " + str(response.json()["currently"]["temperature"]) + " degrees Fahrenheit."
        await self.bot.say(msg)
    
        
def setup(bot):
    bot.add_cog(Weather(bot))
#The last thing to do is to go to the DiscordBot.py and add commands.<insertclassname>
