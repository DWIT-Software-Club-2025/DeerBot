import discord
from discord.ext import commands


class AssignRoles (commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.bot.get_guild(1267684605461266502)
        if guild:
            role = guild.get_role(1311574735389200465)
        await member.add_roles(role, "Member Join Role: Default Role Add")


async def setup(bot):
    await bot.add_cog(AssignRoles(bot))
