#Made by Richyy
import discord
from discord.ext import commands

# Bot setup
intents = discord.Intents.default()
intents.members = True  # Required for accessing member information
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

# Command to ban a specific user
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned. Reason: {reason}")
    except Exception as e:
        await ctx.send(f"Failed to ban {member.mention}. Error: {e}")

# Command to kick a specific user
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked. Reason: {reason}")
    except Exception as e:
        await ctx.send(f"Failed to kick {member.mention}. Error: {e}")

# Run the bot
bot.run("MTMxMDEwOTIxODg2NjU5Mzc5Mg.GRPbG8.MWNvBZNzJ47tbRM9I-MlKZSIaKqVIlV7dewv18")
pip install discord.py
import discord
from discord.ext import commands

# Bot setup
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Command to delete all channels and send a message
@bot.command()
@commands.has_permissions(administrator=True)
async def reset_channels(ctx):
    guild = ctx.guild
    confirmation_message = await ctx.send("Are you sure you want to reset all channels? Reply with `yes` to confirm.")

    def check(msg):
        return msg.author == ctx.author and msg.content.lower() == "yes"

    try:
        await bot.wait_for("message", check=check, timeout=30)
        await confirmation_message.delete()

        # Delete all channels
        for channel in guild.channels:
            await channel.delete()

        # Recreate a general channel
        general_channel = await guild.create_text_channel("general")
        await general_channel.send("@everyone All channels have been reset.")
        await ctx.send("All channels have been reset successfully!")
    except TimeoutError:
        await confirmation_message.delete()
        await ctx.send("Channel reset canceled. You didn't reply in time.")

# Run the bot
bot.run("MTMxMDEwOTIxODg2NjU5Mzc5Mg.GRPbG8.MWNvBZNzJ47tbRM9I-MlKZSIaKqVIlV7dewv18")
