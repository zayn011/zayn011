import asyncio
import os
import urllib

import requests

from userbot import *
from mafiabot.utils import *
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd("zayn$"))
@bot.on(sudo_cmd(pattern="zayn$", allow_sudo=True))
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Z")
    await asyncio.sleep(0.9)
    await a.edit("A")
     await asyncio.sleep(0.9)
    await a.edit("Y")
     await asyncio.sleep(0.9)
    await a.edit("N")
    
@bot.on(admin_cmd("anisha$"))
@bot.on(sudo_cmd(pattern="anisha$", allow_sudo=True))
async def butts(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("A")
    await asyncio.sleep(0.9)
    await a.edit("N")
     await asyncio.sleep(0.9)
    await a.edit("I")
     await asyncio.sleep(0.9)
    await a.edit("S")
     await asyncio.sleep(0.9)
    await a.edit("H")
     await asyncio.sleep(0.9)
    await a.edit("A")
 
CmdHelp("zayn").add_command(
  'zayn', None, 'Sends a random boobs pic'
).add_command(
  'anisha', None, 'Sends a random Butt pic'
).add()
