from ..betterbot import Member
from ..discordbot import (
	has_role,
	unmute_user
)
import discord

name = 'unmoot'
bot_channel = False


async def run(message, member: Member):
	'Removes a moot from a member'

	if not (
		has_role(message.author.id, 717904501692170260, 'helper')
		or has_role(message.author.id, 717904501692170260, 'trialhelper')
	):
		return

	await unmoot_user(
		member.id,
		reason=f'Unmooted by {str(message.author)}'
	)

	await message.send(embed=discord.Embed(
		description=f'<@{member.id}> has been unmooted.'
	))