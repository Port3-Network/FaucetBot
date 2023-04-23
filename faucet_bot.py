# This example requires the 'members' and 'message_content' privileged intents to function.

import os
import sys

from app import create_app
from app import current_app

import discord
from discord.ext import commands
from soquest_api import get_winners

description = '''An example bot using soquest open api, to distribute the token to specified whitelist addresses.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def echo(ctx):
    print('echo')
    await ctx.send('echo to you')

@bot.command()
async def faucet(ctx, address: str):
    """
    Pass the address as a parameter, and then send the token to that address.
    """
    campaign_code = 'gy6930eNFr' # campaign require user to finish
    prize_code = '1682264693-1' # prize match this airdrop

    white_list = get_winners(campaign_code, prize_code)
    if address not in white_list:
        await ctx.send('You are not eligble, Please complete Quest first: \nhttps://soquest.xyz/space/port3network/campaign/gy6930eNFr')
    else:
        # TODO implement send transaction here
        await ctx.send('Token is sent to your address.')


def main():
    bot.run(current_app.config['DISCORD_BOT_TOKEN'])


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        try:
            main()
        except:
            app.logger.exception('something wrong!')
            sys.exit()

