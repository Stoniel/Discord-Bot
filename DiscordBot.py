import discord
import secrets
from discord.ext.commands import Bot

bot = Bot(command_prefix='!')

@bot.event
async def on_read():
    print('Client Logged in')


if __name__ == '__main__':
#add commands.yourCommand with a , outside the quote
    extensions = [
        'commands.counter',
        'commands.template',
        'commands.rps',
        'commands.timer',
        'commands.raids',
        'commands.unix_cmds',
        'commands.dice',
        'commands.translate',
        'commands.weather',
        'commands.trivia'
        
    ]

    for extension in extensions:
            bot.load_extension(extension)

    bot.run(secrets.BOT_TOKEN)
