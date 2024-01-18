import discord
from discord.ext import commands
import random, os
from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            file.save(f'{file_name}')
            await file.save(f'{file_name}')
            await ctx.send(f'file disimpan dengan atas nama{file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)

            if hasil[0] == 'Bunga Heliopsis\n' and hasil[1] >= 0.6:
                await ctx.send('INI ADALAH Heliopsis')
                await ctx.send('Bunga Heliopsis berasal dari Amerika Utara bagian timur dan tengah. Bunga Heliopsis biasanya dinamakan false sunflower')
            elif hasil[0] == 'Bunga Matahari\n' and hasil[1] >= 0.6:
                await ctx.send('INI ADALAH BUNGA MATAHARI')
                await ctx.send('Bunga Matahari berasal dari Meksiko.')
            else:
                await ctx.send('GAMBAR TIDAK VALID')
    else:
        await ctx.send("Anda tidak mengirim apapun??")

bot.run("")