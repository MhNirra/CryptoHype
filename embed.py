import discord

def create_crypto_price_embed(btc_price, eth_price):
    embed = discord.Embed(title="Estado del Mercado", description="Precio actual del Bitcoin(BTC) y Etherium(ETH)",color=16776960)
    embed.add_field(name="Precio Actual", value=f"BTC: ${btc_price}", inline=True)
    embed.add_field(name="Precio Actual", value=f"ETH: ${eth_price}", inline=True)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/805261985268760628/1206716925145780234/eth-btc.png?ex=65dd05b6&is=65ca90b6&hm=389f7e0f5db3f8acda5b10ae4c8dd8748efcd43be7db30cacfbb67f4da21f6e6&=&format=webp&quality=lossless&width=1193&height=671")
    embed.set_footer(text="Información proporcionada por CryptoHype.")
    return embed