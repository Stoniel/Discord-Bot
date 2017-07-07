#@author: Stone Daniel July 2017
import discord
from discord.ext import commands
import json
import requests
import secrets

class Weather:
    def __init__(self,bot):
        self.bot = bot
        
    
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
