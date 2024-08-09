import discord
from discord.ext import commands
import random

greetings = ["hello", "hi", "wassup", "hii", "hola", "namaste", "k cha"]


class Ping(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"The bot latency is {
                round(self.bot.latency * 1000)}ms.",
            color=0xBEBEFE,
        )
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def hello(self, ctx):
        await ctx.channel.send(f"{greetings[random.randint(0, len(greetings))]} {ctx.author.mention}")



async def setup(bot):
    await bot.add_cog(Ping(bot))
