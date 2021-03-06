#@author: Stone Daniel July 2017
import discord
from discord.ext import commands
import json
import requests
import secrets

class Weather:
    def __init__(self,bot):
        self.bot = bot
        self.loc = ''

    def get_coords(self,location):
        geocode = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + location + '&key=' + secrets.geocode_API)
        if geocode.status_code != 200:
            return 0
        self.loc = geocode.json()['results'][0]['address_components'][0]['long_name']
        lat = geocode.json()['results'][0]['geometry']['location']['lat']
        longitude = geocode.json()['results'][0]['geometry']['location']['lng']
        coords = str(lat) + ',' + str(longitude)
        return coords
        
    @commands.command(
        name='weather',
        aliases=[],
        description='Provides a forecast for a desired location',
        brief='Weather',
        pass_context = True,
        run_without_commands = True
    )

    async def weather(self,ctx,*,message):
        coords = self.get_coords(message)
        response = requests.get('https://api.darksky.net/forecast/' + secrets.weather_key + "/" + coords)
        msg = '```' + "The weather in " + self.loc  + " is " + response.json()["currently"]["summary"] + ". It is currently " + str(response.json()["currently"]["temperature"]) + " degrees Fahrenheit." + '```'
        await self.bot.say(msg)

    @commands.command(
        name = 'forecast',
        description = 'Gives a 5 day forecast summary',
        brief = 'Forecast Summary'
    )
    async def forecast(self,ctx,*,message):
        coords = self.get_coords(message)
        response = requests.get('https://api.darksky.net/forecast/' + secrets.weather_key + "/" + coords)
        msg = '```' + response.json()["daily"]["summary"] + '```'
        await self.bot.say(msg)
        
def setup(bot):
    bot.add_cog(Weather(bot))
