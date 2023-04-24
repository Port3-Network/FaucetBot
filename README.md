# FaucetBot
This is a demo for a faucet bot that utilizes the SoQuest open API.

This bot is built using [discord.py](https://discordpy.readthedocs.io/en/stable/).

## Run the bot
To get start, install the requirements:

```
pip3 install -r requirements.txt
```

Create a directory for the bot's logs:

```
mkdir /var/log/faucet_bot/
```

Finally, run the faucet bot:

```
python3 run_faucet_bot.py
```

You can use supervisor or nohup to run the bot as a daemon.


## Try in Discord
Try using the Discord platform to access the faucet bot, or visit the following link to try it [here](https://discord.com/api/oauth2/authorize?client_id=996239519928037437&permissions=116736&scope=bot)
