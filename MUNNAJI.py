from userbot import bot as MUNNAgalaxy
from userbot.utils import admin_cmd as choot

x = True
@MUNNAgalaxy.on(choot(pattern="bsdk"))
async def yashraid(event):
    while x != False:
       
        await event.delete()
        kek = event.chat_id
        a=await MUNNAgalaxy.send_message(kek, "Z")
        await asyncio.sleep(0.9)
    await a.edit("A")
     await asyncio.sleep(0.9)
    await a.edit("Y")
     await asyncio.sleep(0.9)
    await a.edit("N")
