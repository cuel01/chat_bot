import discord
import asyncio
import time

client = discord.Client()

token = "ODM1NDc1ODU1OTExMTU3ODIw.YIP_hg.wH8qu4Bspc52d0-_Gy0NpWR3Zco"

# 디스코드 봇이 실행 됬을 때 작동하는 코드
@client.event
async def on_ready():
    global stop
    print("log_bot start")
    activity = discord.CustomActivity("로그 남기기")
    status=discord.Status.offline
    stop=0
    await client.change_presence(activity=activity, status=status)
    embed = discord.Embed(title="메인 제목", description="설명", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
    embed.set_footer(text="하단 설명") # 하단에 들어가는 조그마한 설명을 잡아줍니다
    await client.get_channel(836766046488231987).send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
    await client.get_channel(836766046488231987).send("할 말", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.

# 디스코드에서 누가 메시지를 보냈을 때 작동하는 코드
@client.event
async def on_message(message):
    global stop
    if str(message.content)=="!멈춰":
        stop=1
    if str(message.content)=="!계속":
        stop=0
    if stop==0:
        msg_log="on_message "+str(message.id)+" <"+str(time.ctime(time.time()))+"> " + str(message.channel.name) + " (id : " + str(message.channel.id) + ") "+str(message.author.name)+ "(# " + str(message.author.discriminator) + ") " +  "(id : "+str(message.author.id)+") " + str(message.content) 
        log_file = open("log.txt", "a",encoding='UTF-8')
        log_file.write(msg_log + "         " + str(message)+"\n")
        log_file.close()
        print(msg_log)
    


# 디스코드에서 누가 메시지를 지웠을 때 작동하는 코드
@client.event
async def on_message_delete(message):
    global stop
    if stop==0:
        msg_log="on_message_delete "+str(message.id)+" <"+str(time.ctime(time.time()))+"> " + str(message.channel.name) + " (id : " + str(message.channel.id) + ") "+str(message.author.name)+ "(# " + str(message.author.discriminator) + ") " +  "(id : "+str(message.author.id)+") " + str(message.content) 
        log_file_a = open("log.txt", "a",encoding='UTF-8')
        log_file_a.write(msg_log + "         " + str(message)+"\n")
        log_file_a.close()
        print(msg_log)
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
