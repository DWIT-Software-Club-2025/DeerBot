import discord
import os
import asyncio

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    await load()
    await bot.start(os.getenv("TOKEN"))


asyncio.run(main())
