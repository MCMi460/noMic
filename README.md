# noMic

*A Discord text-to-speech bot for people without a mic.*

## How to use

### [Download current master.zip][master]

Step 1:

Make a develop application. Then, download master.zip and unzip.

Step 2:

Download all requirements as stated in the requirements section, then update the [settings.py][settings] with your token and prefix of choice.

Step 3:

Type `python3 bot.py` in a commandline.

Step 4:

Invite the bot and do (prefix)help

---

*(In case you haven't heard yet, Discord now has [SLASH Commands!][slashc] However, I'm sorry to disappoint when I say that discord.py has no plans as of now to add support for them in an update. Until their decision is changed and support is added, there will not be an update for this repository with slash commands. The main function of this bot and all of its commands are unaffected by this, but the visual integration of commands on a client's display is not available. Thank you.)*

---
## Requirements:

-[Python 3.9.0][python]
<br>-[discord.py][discordpy]
<br>-[FFmpeg][ffmpeg]
<br>-[gTTS][gtts]

*(All requirements used visible in [bot.py][bot])*

---
If you have any issues, [contact me here][support].

You don't have to give credit to me. That's not what Github is for (in my opinion).

<a href="https://mi460.dev/github"><img src="https://img.shields.io/static/v1?label=MCMi460&amp;message=Github&amp;color=c331d4"></a>
<a href="https://mi460.dev/discord"><img src="https://discordapp.com/api/guilds/699728181841887363/embed.png"></a>

[gtts]: https://pypi.org/project/gTTS/
[ffmpeg]: https://pypi.org/project/ffmpeg/
[settings]: https://github.com/MCMi460/noMic/blob/main/settings.py
[master]: https://github.com/MCMi460/noMic/archive/main.zip
[python]: https://www.python.org/downloads/
[discordpy]: https://github.com/Rapptz/discord.py/blob/master/README.rst
[bot]: https://github.com/MCMi460/noMic/blob/main/bot.py
[support]: https://mi460.dev/bugs
[slashc]: https://discord.com/developers/docs/interactions/slash-commands
