import random

import discord
from discord.ext import commands, tasks


class Status(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @tasks.loop(minutes=1.0)
    async def status_task(self) -> None:

        statuses = ["with you!", "powered by Software Club 2025"]
        await self.change_presence(activity=discord.Game(random.choice(statuses)))

    @status_task.before_loop
    async def before_status_task(self) -> None:
        """
        Before starting the status changing task, we make sure the bot is ready
        """
        await self.wait_until_ready()


async def setup(bot):
    await bot.add_cog(Status(bot))
