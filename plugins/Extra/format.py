import time
import random
from pyrogram import Client, filters

CMD = ["/", ".","@"]

@Client.on_message(filters.command("format", CMD))
async def format(_, message):
    await message.reply_text("""<b><blockquote>Only Send the movie name to the group</blockquote></b>

<b>Format :-</b>

<b>For movie :- </b><code>movie name (as per in Google) year of release</code>

<b>For series :- </b><code>series name (as per in Google) S(SEASON NO) E(EPISODE NO)</code>

<b>EXAMPLE :- </b>

<b>MOVIE :- </b><code>Brahmastra Part One Shiva 2022</code>

<b>Series :- </b><code>The Flash S01 E10</code>
""")

