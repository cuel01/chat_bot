import discord
import asyncio
import time

client = discord.Client()

token = "ODM1NDc1ODU1OTExMTU3ODIw.YIP_hg.wH8qu4Bspc52d0-_Gy0NpWR3Zco"

@client.event
async def on_ready():
    print("chat_bot start")
    channel_id=775223797250392068
    while True:
        msg=input()
        if "!channel " == msg[0:9]:
            channel_id=int(msg[9:27])
            print(channel_id)
        else: 
            await client.get_channel(channel_id).send(msg)

client.run(token)

'''
소통방 775223797250392068
크시 816299664251813938

'''
