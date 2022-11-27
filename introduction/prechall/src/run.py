from discord.ext import commands
from random import choice
import discord

messages = ["Le mot de passe n'est pas bon, retentez votre chance en bon perdant !", "Je n'ai pas compris, pouvez-vous répéter plus fort s'il vous plaît ?", "Il m'apparaît évident que ce n'est pas la réponse attendue...", "Peut-être que si vous étiez un poil plus poli ça se passerait mieux :neutral_face:.","La réponse est dans votre coeur, malheureusement elle est juste fausse"]
bot = commands.Bot(command_prefix="+", help_command=None,intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} s\' est connecté à Discord!')

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.DMChannel):
        canal = bot.get_channel(1038099165663727738)
        if(message.author.id != 1038093755036737596):
            if(message.content == "S3cReTFlaG_Mal0!!"):
                await message.channel.send("Oh, bonjour ! Invitez-moi à prendre une tasse de thé pour que nous puissions discuter. :teapot:\nPS: essayez `+secret`")
                await canal.send(f"{message.author.mention} a trouvé le mot de passe !")
            else:
                mess = choice(messages)
                await message.channel.send(mess)
                await canal.send(f"{message.author.mention}: {message.content}")
                await canal.send(f"Réponse: {mess}")
    else:   
        if(message.author.id != 1038093755036737596):
            if(message.content.startswith('+')):
                if(message.content == "+secret"):
                    if(message.author.guild_permissions.administrator):
                        await message.channel.send("Bonjour maître, voici votre secret: https://bwlryq.net/super_executable_for_my_master_only")
                    else:
                        await message.channel.send("Vous n'êtes pas mon maître, pourquoi vous donnerais-je mon secret ?")
                else:
                    await message.channel.send("Commande non reconnue")

bot.run("BOT-TOKEN-HERE")