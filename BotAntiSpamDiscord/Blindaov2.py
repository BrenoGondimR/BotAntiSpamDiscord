import discord
from discord.ext import commands
import asyncio



client = commands.Bot(command_prefix="!")

##########-AntiSpam-###########

@client.event
async def on_ready():
    print("Ready")
    while True:
        print("Clear")
        await asyncio.sleep(10)
        with open("spam_detect.txt", "r+") as file:
            file.truncate(0)


@client.event
async def on_message(message):
    counter = 0
    with open("spam_detect.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter+=1


        file.writelines(f"{str(message.author.id)}\n")
        if counter > 5:
            await message.guild.ban(message.author, reason="Spam")
            await asyncio.sleep(1)
            await message.guild.unban(message.author)
            print("OPS")


############-DeletarCanal-###############
@client.event
async def delete_channel(ctx, channel_name):
    # check if the channel exists
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)

    # if the channel exists
    if existing_channel is not None:
            await existing_channel.delete()
    # if the channel does not exist, inform the user
    else:
        await ctx.send(f'No channel named, "{channel_name}", was found')


client.run("")