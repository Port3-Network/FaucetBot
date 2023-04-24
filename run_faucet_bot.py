#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

from app import create_app
from flask import current_app

import discord
from discord.ext import commands
from app.faucet_bot import DiscordRobot


def main():
    bot_id = current_app.config['CURRENT_DISCORD_BOT_ID']

    intents = discord.Intents.all()
    discord_bot = commands.Bot(command_prefix='!', intents=intents)

    discord_bot.add_cog(DiscordRobot(bot_id, discord_bot))
    discord_bot.run(current_app.config['DISCORD_BOT_TOKEN'])


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        try:
            main()
        except:
            app.logger.exception('process fail')
            sys.exit()

