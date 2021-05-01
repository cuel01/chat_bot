import discord
import asyncio
import os

client = discord.Client()

token = os.environ["BOT_TOKEN"]

@client.event
async def on_ready():
    print("chat_bot start")
    channel_id=int(input("최초 생성 채널 id"))
    while True:
        msg=input()
        if "!channel " == msg[0:9]:
            channel_id=int(msg[9:27])
            print(channel_id)
        else: 
            await client.get_channel(channel_id).send(msg)

client.run(token)
