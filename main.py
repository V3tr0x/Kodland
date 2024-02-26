from bot_logic import gen_pass, gen_emodji, flip_coin, double_letter, number, marynarzyk 
import discord

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$help'):
        await message.channel.send("Jeśli masz jakiś problem spróbuj skontaktować się z administratorem serwera")
    elif message.content.startswith('$nuda'):
        await message.channel.send("@everyone")
    elif message.content.startswith('$bye'):
        await message.channel.send("bye")
    elif message.content.startswith('$liczba'):
        await message.channel.send(number())
    elif message.content.startswith('$marynarzyk'):
        await message.channel.send(marynarzyk())
    elif message.content.startswith('11'):
        await message.channel.send('emoji:'+gen_emodji())
    elif message.content.startswith('12'):
        await message.channel.send('moneta:'+flip_coin())
    elif message.content.startswith('$podwójnalitera'):
        await message.channel.send(double_letter('Witaj'))
    elif message.content.startswith('$hasło'):
        await message.channel.send('Twoje hasło to' +gen_pass(10))
    else:
        await message.channel.send("błąd")

client.run("MTIwOTE4NTM2ODYyMTA2NDI1Mg.G-LONm.USLicx9l5CgX0f0sqonakbT4em2k-AC0Lu6Npg")
