import discord

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!help'):
        msg = 'Current commands are: !help,!raids {0.author.mention}'.format(message)
    if message.content.startswith('!raids'):
        msg = 'https://gyazo.com/3bbeed8086082e9ff9b8e652f1f9f091 {0.author.mention}'.format(message)
    if message.content.startswith('!count'):
        
    await client.send_message(message.channel,msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.id)

client.run('MzIwMzM3MzI3NjgxNTY4NzY4.DCjH9g.ynp58ZpkyyJPB72L34mhCtHC8ak')
