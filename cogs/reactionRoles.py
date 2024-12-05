import discord
from discord.ext import commands


class ReacitonRoles(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.bot.reaction_roles = []
        self.reaction_message = int()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        for role, ms, emoji in self.bot.reaction_roles:
            if ms.id == payload.message_id and emoji == payload.emoji.name:
                await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        for role, msg, emoji in self.bot.reaction_roles:
            if msg.id == payload.message_id and emoji == payload.emoji.name:
                try:
                    await self.bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

                except Exception as e:
                    print(f"An error occurred: {str(e)}")

    @commands.command()
    async def set_reaction_role(self, ctx, role: discord.Role, emoji):
        try:

            embed = discord.Embed(
                title=f"Get Your Role for {role.name}",
                description=f"Role: {role.mention}\nEmoji: {emoji}",
                color=discord.Color.green()
            )
            message = await ctx.send(embed=embed)
            await message.add_reaction(emoji)
            self.bot.reaction_roles.append((role, message, emoji))
            self.reaction_message = message.id
        except discord.errors.HTTPException:
            await ctx.send("Invalid emoji provided.")

        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")


async def setup(bot):
    await bot.add_cog(ReacitonRoles(bot))
