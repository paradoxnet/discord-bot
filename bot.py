import asyncio
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # bot allowed to read messages 

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def repeat(ctx, times: int, *, message: str):
    times = min(times, 10_000)  # limit to avoid crashing lol
    for _ in range(times):
        await ctx.send(message)
        await asyncio.sleep(0.1)  # delay bc crash AGAIN

async def keep_alive():
    while True:
        try:
            await bot.start(os.getenv("TOKEN"))  #  read token from environment variable
        except Exception as e:
            print(f"⚠️ Bot crashed: {e}. Restarting in 5 seconds...")
            await asyncio.sleep(5)

asyncio.run(keep_alive())  # auto reconnect if crashed cuzim not advanced