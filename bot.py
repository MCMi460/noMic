import discord
from discord.ext import commands, tasks
import asyncio
from discord.utils import get
from discord.ext.tasks import loop
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
from settings import token, prefix, activity
from gtts import gTTS

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=prefix,intents=intents)
typeStatusListen = discord.ActivityType.listening
bot.remove_command("help")

vc = None
userenabled = None

@bot.event
async def on_message(message):
    if userenabled:
        if message.author == userenabled:
            text = message.content
            name = message.author.name
            channel = message.author.voice.channel
            if not channel:
                pass
            elif text.startswith("http"):
                pass
            elif len(text) > 100:
                pass
            else:
                text = f"{userenabled.display_name} said " + text
                language = 'en'
                myobj = gTTS(text=text, lang=language, slow=False)
                myobj.save("text.mp3")
                text = discord.FFmpegPCMAudio('text.mp3')
                player = vc.play(text)
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print(f'Present in {len(bot.guilds)} servers.')
    print('------')
    status = f"{activity}"
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=typeStatusListen, name=status))

@bot.command(pass_context=True)
async def help(ctx):
    await ctx.send(f"Sending a help message to your DMs, {ctx.author.mention}.")
    embed = discord.Embed(title="Report a bug", url="https://mi460.dev/bugs", colour=discord.Colour(0x4287f5), description="*noMic allows a user without a mic to speak in a voice channel by typing in a text channel.*")

    embed.set_author(name="noMic")

    embed.add_field(name="`/say`", value="Says the message following this command.", inline=False)
    embed.add_field(name="`/choose`", value="Every message you type from now on (other than links) will be on the voice channel. This will overwrite the previous user.", inline=False)
    embed.add_field(name="`/join`", value="Joins the voice channel you are in.", inline=False)
    await ctx.author.send(embed=embed)

@bot.command(name='join',aliases=['start'])
async def join(ctx):
    name = ctx.author.name
    channel = ctx.author.voice.channel
    global vc
    try:
        vc = await channel.connect()
    except:
        await ctx.send(f"I'm already in a voice channel.")

@bot.command(name='disconnect',aliases=['leave'])
async def disconnect(ctx):
    global vc
    if not vc:
        await ctx.send(f"I'm already not in a voice channel.")
        return
    await vc.disconnect()
    vc = None
    global userenabled
    userenabled = None

@bot.command(name='choose')
async def choose(ctx):
    global userenabled
    userenabled = ctx.author
    await ctx.send(f"{ctx.author.mention} is now chosen! ('{ctx.author.display_name}' will be said before their messages)")

@bot.command(name='say')
async def say(ctx,*,text = None):
    if text:
        language = 'en'
        text = f"{ctx.author.display_name} said " + text
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("text.mp3")
        text = discord.FFmpegPCMAudio('text.mp3')
        player = vc.play(text)
    else:
        await ctx.send(f"{ctx.author.mention}, please specify a message.")

bot.run(token)
