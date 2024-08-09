import discord
from discord.ext import commands

from lyricsgenius import Genius


class LyricsFetcher(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx, *, message: str):
        genius = Genius(
            "1HOLLpdXnmHIrsTxRP902QTolT1V3fmL-1fMZ93kOWAmJEbV1CKBR4Mc4H4nRnrWFsFaSoVLFZP3Dj2iJ46G8Q")

        song = genius.search_song(message)
        embed = discord.Embed(
            title=f"🎵 {message.upper()}",
            description=f"{song.lyrics}",
            color=0xBEBEFE,
        )
        print(song.lyrics)
        await ctx.channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(LyricsFetcher(bot))
