import asyncio

from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"zayn$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"zayn$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 21)
    animation_chars = [
        "`Z `",
        "`ZA`",
        "`ZAY`",
        "`ZAYN`",
        ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 21])

@bot.on(admin_cmd(pattern=r"anisha$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"anisha$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 21)
    animation_chars = [
        "`A `",
        "`AN`",
        "`ANI`",
        "`ANIS`",
        "`ANISH `",
        "`ANISHA`",
        ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 21])
