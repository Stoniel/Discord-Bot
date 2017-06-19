import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix='!')

@bot.event
async def on_read():
    print('Client Logged in')

@bot.command()
async def helpme(*args):
    return await bot.say('Current Commands = !help')

if __name__ == '__main__':

    extensions = [
        'commands.counter'
    ]

    for extension in extensions:
            bot.load_extension(extension)

bot.run('MzIwMzM3MzI3NjgxNTY4NzY4.DCjH9g.ynp58ZpkyyJPB72L34mhCtHC8ak')