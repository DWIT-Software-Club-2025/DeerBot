import discord
from discord.ext import commands


class RenameChannel (commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.bot.get_guild(1267684605461266502)
        if guild:
            channel = guild.get_channel(1311573489295294524)
            members = guild.member_count
        await channel.edit(name=f'members-{members}')
        # await member.add_roles(['Member'])

    @commands.Cog.listener()
    async def on_member_remove(self, guild):
        print("Hello from leave")
        guild = self.bot.get_guild(1267684605461266502)
        if guild:
            channel = guild.get_channel(1311573489295294524)
            members = guild.member_count
        await channel.edit(name=f'members-{members}')


async def setup(bot):
    await bot.add_cog(RenameChannel(bot))
