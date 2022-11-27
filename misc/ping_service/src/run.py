from discord.ext import commands
import re
import discord
from subprocess import PIPE, run

bot = commands.Bot(command_prefix="*", help_command=None,intents=discord.Intents.default())

def exec(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

@bot.event
async def on_ready():
    print(f'{bot.user} s\' est connecté à Discord! [Ping Service]')

@bot.command("help")
async def display_help(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send(
"""
```ini
[Help menu]
```
`*help` → Affiche ce menu
`*pong` → Renvoie "ping"
`*ping <IP>` → Permet de pinger un équipement distant
"""
    )

@bot.command("pong")
async def ping(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("Ping")

@bot.command("ping")
async def debug(ctx, *, code):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        length = len(ctx.message.content)
        if length == 0:
            await ctx.send("Vous n'avez pas spécifié d'adresse IP, merci de réessayer")
            return
        if length > 20:
            await ctx.send(f"{length} caractères, {length-20} de trop ! :angry: Vous n'avez pas besoin de plus de 15 caractères pour une adresse IPv4 mais je vous en donne 20...")
            return
        if "\t" in code or "\n" in code or " " in code:
            code = code.replace(" ","")
            code = code.replace("\t","")
            code = code.replace("\n","")
            await ctx.send("Eh ! Vous n'avez pas besoin d'espaces pour écrire une adresse IP, qu'essayez vous de faire ? :rage:")
            return
        code = "ping -c 1 "+code
        try:
            output = exec(code)
            if(len(output)==0):
                code = code.replace("ping -c 1 ", "")
                output = "ping: "+code+": Name or service not known"
            await ctx.send(f"Voici le résultat de votre ping:\n```{output}```")
        except Exception as e:
            await ctx.send("Erreur, merci de réessayer")

bot.run("YOUR-BOT-TOKEN-HERE")