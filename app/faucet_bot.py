#!/usr/bin/python3
# -*- coding: utf-8 -*-
import discord

from flask import current_app
from discord.ext import tasks
from discord.ext import commands
from soquest_api import get_winners


class DiscordRobot(commands.Cog):
    def __init__(self, bot_id, bot):
        self.bot = bot
        self.bot_id = bot_id

    @commands.command(name='ping')
    async def ping(self, ctx):
        print('ping/pong')
        await ctx.channel.send('pong!')

    @commands.command(name='faucet')
    async def faucet(self, ctx, address: str):
        """
        Pass the address as a parameter, and then send the token to that address.
        """
        campaign_code = 'gy6930eNFr' # campaign require user to finish
        prize_code = '1682264693-1' # prize match this airdrop

        white_list = get_winners(campaign_code, prize_code)
        if address not in white_list:
            await ctx.channel.send('You are not eligble, Please complete Quest first: \nhttps://soquest.xyz/space/port3network/campaign/gy6930eNFr')
        else:
            # TODO implement send transaction here
            await ctx.channel.send('Token is sent to your address.')

