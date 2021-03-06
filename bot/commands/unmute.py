from ..betterbot import Member
from ..discordbot import (
	has_role,
	unmute_user
)
import discord

name = 'unmute'
bot_channel = False


async def run(message, member: Member):
	'Removes a mute from a member'

	if not (
		has_role(message.author.id, 717904501692170260, 'helper')
		or has_role(message.author.id, 717904501692170260, 'trialhelper')
	):
		return

	await unmute_user(
		member.id,
		reason=f'Unmuted by {str(message.author)}'
	)

	await message.send(embed=discord.Embed(
		description=f'<@{member.id}> has been unmuted.'
	))
