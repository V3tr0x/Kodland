import discord, random, os, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    img_name=random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def co_wrzucic_do_zoltego_kosza(ctx):
    with open(f'kosze/butelka.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('O to najpopularniejsza rzecz wrzucana do żółtego kosza')    
    await ctx.send(file=picture)
    await ctx.send('Do żółtego kosza możesz wrzucać też inne przedmioty składające się z plastiku')

@bot.command()
async def co_wrzucic_do_zielonego_kosza(ctx):
    with open(f'kosze/szklo.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('O to najpopularniejsza rzecz wrzucana do zielonego kosza')    
    await ctx.send(file=picture)
    await ctx.send('Do zielonego kosza możesz wrzucać też inne przedmioty składające się z szkła')

@bot.command()
async def co_wrzucic_do_niebieskiego_kosza(ctx):
    with open(f'kosze/papier.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('O to najpopularniejsza rzecz wrzucana do niebieskiego kosza')    
    await ctx.send(file=picture)
    await ctx.send('Do niebieskiego kosza możesz wrzucać też inne przedmioty składające się z papieru')

@bot.command()
async def co_wrzucic_do_czarnego_kosza(ctx):
    with open(f'kosze/czarny.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('O to przykład rzeczy wrzucanej do czarnego kosza')    
    await ctx.send(file=picture)
    await ctx.send('Do czarnego kosza możesz wrzucać wyroby skórzane i z futra, ubrania, obuwie czy zużyte naczynia, a także żwirek i odchody zwierząt.  Oprócz tego do czarnego kosza wrzuca się resztki jedzenia pochodzenia zwierzęcego, takie jak ser, jajka i nabiał, a także mięso czy kości.')

@bot.command()
async def co_wrzucic_do_czerwonego_kosza(ctx):
    with open(f'kosze/metal.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('O to rzecz wrzucana do czerwonego kosza')    
    await ctx.send(file=picture)
    await ctx.send('Kosz czerwony jest rzadko spotykany, jednak wrzucamy do niego głównie puszki i drobny złom zrobiony z metalu. Jeżeli w pobliżu nie ma czewonego kosza puszka tą można wrzucić do żółtego pojmnika. Nie wrzucamy jednak np. baterii lub pojemnika po lakierze')

@bot.command()
async def gdzie_wrzucac_bio_odpady(ctx):
    with open(f'kosze/bio.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('Na zdjęciu jest pokazany brązowy kosz')    
    await ctx.send(file=picture)
    await ctx.send('Brązowy kosz ma najczęściej napis bio.')






























bot.run("MTIwOTE4NTM2ODYyMTA2NDI1Mg.GHAfgB.oOkyMOEvpn-qS5ol8yIUKCbkz1may9YdhPRbWM")
