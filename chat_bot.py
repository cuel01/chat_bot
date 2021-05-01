import discord
import asyncio
import os

client = discord.Client()

token = 

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
