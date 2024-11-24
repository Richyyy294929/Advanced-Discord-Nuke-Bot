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
bot.run("MTMxMDEwOTIxODg2NjU5Mzc5Mg.GRPbG8.MWNvBZNzJ47tbRM9I-MlKZSIaKqVIlV7dewv18") pip install discord.py
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
bot.run("MTMxMDEwOTIxODg2NjU5Mzc5Mg.GRPbG8.MWNvBZNzJ47tbRM9I-MlKZSIaKqVIlV7dewv18")pip install discord.py
