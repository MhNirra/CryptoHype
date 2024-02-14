import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from data import get_btc_price_history, get_eth_price_history
from embed import create_crypto_price_embed

load_dotenv()
TOKEN = os.getenv('TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

async def send_btc_price():
    btc_price = get_btc_price()
    eth_price = get_eth_price()
    embed = create_crypto_price_embed(btc_price, eth_price)
    webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.RequestsWebhookAdapter())
    if webhook:
        await webhook.send(embed=embed, username='CryptoHype')
    else:
        print("Error")

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} Conectado!')
    await send_btc_price()
    send_btc_price_task.start() 

@tasks.loop(minutes=2)
async def send_btc_price_task():
    await send_btc_price()

bot.run(TOKEN)