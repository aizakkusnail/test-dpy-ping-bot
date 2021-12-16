import discord, os
from discord.ext import commands
from discord.ext.commands import CommandNotFound

client = commands.Bot(
    command_prefix=commands.when_mentioned_or("c."),
    intents=discord.Intents.default(),
    activity=discord.Game(name="c.chat with randos"),
    status=discord.Status.idle
)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{client.user.name}#{client.user.discriminator} is now up and running.")
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'Woops, you still got `{round(error.retry_after, 2)}` seconds before you can use the command again')
        return
    raise error

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    await ctx.send(f"Pong ({round(client.latency * 1000)}ms)")

client.run(TOKEN)
