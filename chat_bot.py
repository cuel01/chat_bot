import discord
import asyncio
import time
import os

client = discord.Client()

token = os.environ["BOT_TOKEN"]

# 디스코드 봇이 실행 됬을 때 작동하는 코드
@client.event
async def on_ready():
    activity = discord.CustomActivity("로그 남기기")
    status=discord.Status.online
    await client.change_presence(activity=activity, status=status)

# 디스코드에서 누가 메시지를 보냈을 때 작동하는 코드
@client.event
async def on_message(message):
    msg_log="on_message "+str(message.id)+" <"+str(time.ctime(time.time()))+"> " + str(message.channel.name) + " (id : " + str(message.channel.id) + ") "+str(message.author.name)+ "(# " + str(message.author.discriminator) + ") " +  "(id : "+str(message.author.id)+") " + str(message.content) 
    log_file = open("log.txt", "a",encoding='UTF-8')
    log_file.write(msg_log + "         " + str(message)+"\n")
    log_file.close()
    


# 디스코드에서 누가 메시지를 지웠을 때 작동하는 코드
@client.event
async def on_message_delete(message):
    msg_log="on_message_delete "+str(message.id)+" <"+str(time.ctime(time.time()))+"> " + str(message.channel.name) + " (id : " + str(message.channel.id) + ") "+str(message.author.name)+ "(# " + str(message.author.discriminator) + ") " +  "(id : "+str(message.author.id)+") " + str(message.content) 
    log_file_a = open("log.txt", "a",encoding='UTF-8')
    log_file_a.write(msg_log + "         " + str(message)+"\n")
    log_file_a.close()
    if int(message.author.id) == 835475855911157820:
        await message.channel.send(str(message.content))
    else:
        log_file_r = open("log.txt", "r",encoding='UTF-8')
        log_file_text=log_file_r.read()
        for i in range(len(log_file_text.split("\n"))-3, 0, -1):
            if str(log_file_text.split("\n")[i].split(" ")[0])=="on_message" and int(str(log_file_text).split("\n")[i].split()[1])==message.id:
                await message.channel.send(" ".join(log_file_text.split("\n")[i].split(" ")[2:7])+" "+str(message.author)+" : "+str(message.content))
                break
        await message.channel.send("날짜 추정 불가 "+str(message.author)+" : "+str(message.content))
        
client.run(token)
