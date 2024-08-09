import discord
from discord.ext import commands
from discord import Guild
del_words = ["deerhack is bad", "we hate code",
             "i hate code", "fuck", "motherfucker", "dipan is bad"]

chake_hate = ["randi chake", "chake bhalu", "pragalva gay"]


class Moderation(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):

        if ctx.author != self.bot.user:
            if str(ctx.content.lower()) in del_words:
                await ctx.delete()

                embed = discord.Embed(
                    title="Message Deleted 🗑️",
                    description=f"The message by {
                        ctx.author.mention} was deleted because user is   a nigger",
                    color=0xBEBEFE,
                )
                await ctx.channel.send(embed=embed)

        if ctx.author != self.bot.user:
            if str(ctx.content.lower()) in chake_hate:

                embed = discord.Embed(
                    title="Bravo🔥🔥",
                    description=f"Thats the spirit {
                        ctx.author.mention} you are a ture warrior",
                    color=0xBEBEFE,
                )
                await ctx.channel.send(embed=embed)

        return

    @commands.command()
    @commands.has_role("MOD")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if reason is None:
            reason = "No reason provided"
        embed = discord.Embed(
            title="⛔ User Banned",
            description=f"The user {member.mention} was banned.",
            color=0xBEBEFE,
        )
        await ctx.send(embed=embed)
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_role("MOD")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        guild = Guild()
        if reason is None:
            reason = "No reason provided"
        try:
            await member.kick(reason=reason)
            all_members = guild.fetch_member()
            if member not in all_members:
                embed = discord.Embed(
                    title="⛔ User Kicked",
                    description=f"The user {member.mention} was kicked.",
                    color=0xBEBEFE,
                )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I do not have permission to kick this user.")
        except discord.HTTPException as e:
            await ctx.send(f"An error occurred: {e}")


async def setup(bot):
    await bot.add_cog(Moderation(bot))
