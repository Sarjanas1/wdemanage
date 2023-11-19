# Variable created is grey
# recode by Rexa
# Gausah hapus memek


import os
import random
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterVideo, InputMessagesFilterVoice
from KynanRobot.events import register
from KynanRobot import telethn as tbot, ubot2                 


@register(pattern="^/asupan ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Video Asupan...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@Database_TonicUbot", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Asupan nya Kak 🥵", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  


@register(pattern="^/ppanime ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari PP Anime...🇯🇵**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih pp animenya", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("PP animenya ga ada")  


@register(pattern="^/wallanime ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Wallpaper Anime...🇯🇵**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@Anime_WallpapersHD", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Wallpaper Animenya", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Wallpaper Animenya Kosong")  

@register(pattern="^/asv ?(.*)")
async def _(event):
    memeks = await event.reply("**Sedang Memproses...⛩️**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@anime_status998", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Anime Short Video By [Zenitsu](https://t.me/zenitsuuuxrobot)", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  

@register(pattern="^/desah ?(.*)")
async def _(event):
    memeks = await event.reply("**sabar kak...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@deshanhiroshi", filter=InputMessagesFilterVoice
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Desahannya kak 🥵", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  

@register(pattern="^/ayang ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari ayang...💕**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih kak ayang nya", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  
        
        
@register(pattern="^/sadvid ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari video sedih...**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@sadvideorexa", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Jangan terlalu sedih ya kak", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  
        
@register(pattern="^/funvid ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari video Lucu...**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@videolucuxauserbot", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Funny Video by [Zenitsu](https://t.me/zenitsuuuxrobot)", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada koncol")  
        
@register(pattern="^/ttfyp ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari video fyp...**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@cah0192837465", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Tiktok FYP video by [Zenitsu](https://t.me/zenitsuuuxrobot)", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada koncol")  
        
@register(pattern="^/memeid ?(.*)")
async def _(event):
    memeks = await event.reply("**Tunggu Sebentar...**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@meme_comic", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Meme ID by [Zenitsu](https://t.me/zenitsuuuxrobot)", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada koncol")  
        
@register(pattern="^/ppcp ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Mentahan Foto Couple ...**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@mentahanppcp", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Mentahan PP couple by [Zenitsu](https://t.me/zenitsuuuxrobot)", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  
        
@register(pattern="^/phub?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Bokep....**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@notygirl", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Negative Content by [Zenitsu](https://t.me/zenitsuuuxrobot)", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  
        
@register(pattern="^/nudphot ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Foto Bugil...**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@durovbgst", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Adult Photos by [Zenitsu](https://t.me/zenitsuuuxrobot)", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol") 
        
@register(pattern="^/ayg ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari ayang...💕**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@papcowo", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih kak ayang nya", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")       


__mod_name__ = "ᴀꜱᴜᴘᴀɴ"

__help__ = """
 ──「 ᴀꜱᴜᴘᴀɴ 」──

➣ *Perintah yang tersedia:*

1️⃣ *Special Video*
ᐉ /asupan*:* Untuk mendapatkan video secara acak.
ᐉ /ttfyp*:* Untuk Mendapatkan Video dari tiktok
ᐉ /sadvid*:* Untuk Mendapatkan Sad Video Secara Random
ᐉ /funvid*:* Untuk Mendapatkan Video Lucu Secara Random

2️⃣ *Special Voice*
ᐉ /desah*:* Untuk mendapatkan desahan secara acak

3️⃣ *Special Foto*
ᐉ /ayang*:* Untuk mendapatkan ayang mu (sering digunakan oleh jomblo)
ᐉ /memeid*:* Untuk Mendapatkan Foto Meme Secara Random
ᐉ /ppcp*:* Untuk Mendapatkan Mentahan PP couple Secara Random
"""
