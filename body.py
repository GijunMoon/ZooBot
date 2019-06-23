#import Bot Lib
import asyncio
import discord
import os

app = discord.Client() #discord.Client as app

#Bot System Line
@app.event
async def on_ready():
    print("다음으로 로그인합니다. :  ")
    print(app.user.name)
    print(app.user.id)
    print("===========")
    #Bot's play gmae stats
    await client.change_presence(game=discord.Game(name="동물원에 오신 것 을 환영합니다.", type=1))


#Bot send new message
@app.event
async def on_message(message):
    if message.autor.bot:
        return None #sent was bot
    if message.content == "커맨드": #sent was user
        await app.send_message(message.channel, "답변")


access_token = os.environ["BOT_TOKEN"]
app.run(access)
