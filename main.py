import discord
from discord.ext import commands, tasks
from datetime import time

Token = 'MTQ4MjMyNTY4MjE3NTQ3NTg3Mw.GTBGKO.vWZ_uXGsQx0KVRuValhXT_saig831RZFa-Vl60'
Channel_id = 1482327396194713674 #1482330205250125958




intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@tasks.loop(hours=24)
async def menel_przypomnienie():
    channel = bot.get_channel(Channel_id)
    if channel:
        gif = "https://media.discordapp.net/attachments/1257023017503035497/1314673689345785896/ezgif-6-c4a8d5d4fe-1.gif?ex=69b65e88&is=69b50d08&hm=eed237361361f574943e2dc9d33e2134195e0bac2daedad6320263e6c02f88d6&=&width=400&height=400"
        await channel.send(f"@everyone! Przypominam, że Mateusz pobił menela, i dlatego obchodzimy kolejny dzień na emigracji w Rumunii \n{gif}")
    if channel is None:
        print(f"BŁĄD: Nie znaleziono kanału o ID {CHANNEL_ID}. Sprawdź uprawnienia bota!")
        return

@menel_przypomnienie.before_loop
async  def before_msg():
    print('Czekam...')
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name} (ID: {bot.user.id})')
    if not menel_przypomnienie.is_running():
        menel_przypomnienie.start()
    print ('Machina ruszyła skurwielu.')

@bot.command()
async def czesc(ctx):
    await ctx.send(f'Cześć {ctx.author.mention}! Melduję się na posterunku! 🫡')

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Opóźnienie: {latency}ms')


bot.run(Token)