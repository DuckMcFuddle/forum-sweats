from ..betterbot import Member
from ..discordbot import has_role
from datetime import datetime
import db

name = 'clearinfractions'
bot_channel = False


async def run(message, member: Member, date: str = None):
	'Checks the infractions that a user has (mutes, warns, bans, etc)'

	if (
		not has_role(message.author.id, 717904501692170260, 'helper')
		and not has_role(message.author.id, 717904501692170260, 'trialhelper')
	):
		return

	if not member or not date:
		return await message.send('Please use `!clearinfractions @member date`')
	# month, day, year = date.split('/')
	if date == 'today':
		date = datetime.now()
	else:
		try:
			date = datetime.strptime(date.strip(), '%m/%d/%Y')
		except ValueError:
			return await message.send('Invalid date (use format mm/dd/yyyy)')
	cleared = await db.clear_infractions(member.id, date)

	if cleared > 1:
		return await message.send(f'Cleared {cleared} infractions from that date.')
	if cleared == 1:
		return await message.send('Cleared 1 infraction from that date.')
	else:
		return await message.send('No infractions found from that date.')
