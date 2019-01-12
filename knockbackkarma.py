import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import os

client = commands.Bot(command_prefix = '=')
client.remove_command('help')
status = ['ALPHA | v0.0.3', 'Coming soon: =help & =info', 'Coming soon: Moderation commands!', 'Coming soon: Fun commands!']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(20)

@client.event
async def on_ready():
    print('I am ready!')

@client.event
async def on_message(message):
    print('A user has sent a message.')
    await client.process_commands(message)

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command(pass_context=True)
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages have been deleted.')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Help')
    embed.add_field(name='=ping', value='Returns a Pong!', inline=False)

    await client.send_message(author, embed=embed)

client.loop.create_task(change_status())
client.run(os.getenv('TOKEN'))

