import discord
from discord.ext import commands
import asyncio
import random

class fluff():
	def __init__(self, bot):
		self.bot = bot


	@commands.command(description="Checks the bot's pulse")
	async def ping(self):
		await self.bot.say("pong!")

	@commands.command(pass_context=True, description="Says hello to a user")
	async def hello(self, ctx):
		if ctx.message.author.name == "Cryrore":
			await self.bot.say("Hello, " + str(ctx.message.author.name) + \
				"! Spaghetti and meatballs")

		else:
			await self.bot.say("Hiya, " + str(ctx.message.author.name) + "!")

	@commands.command(description="Chooses randomly")
	async def choose(self, *choices : str):
		await self.bot.say(random.choice(choices))

	@commands.command(description="Screws with the people who try to summon Tunebot")
	async def summon(self):
		await self.bot.say("http://i.imgur.com/z5Vayfy.jpg")

	@commands.command(description="Gives a link to the repos")
	async def github(self):
		await self.bot.say("https://github.com/Lythios/Discord-Chatbot/")


def setup(bot): # I have no idea what this does but it makes the bot work
	bot.add_cog(fluff(bot))