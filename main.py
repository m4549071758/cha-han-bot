import discord
import random
import asyncio
import re

TOKEN = "YOUR_TOKEN_HERE"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"{client.user.name}としてログインしました")
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return #自分自身のアクションは無視
    try:
        if client.user.mentioned_in(message): #メンションされたら
            s = message.content #検索対象文字列指定
            p = r">(.*)" #正規表現で検索範囲設定
            m = re.search(p, s) #ユーザーIDを削除
            _message = m.group(1).replace(" ", "") #空白を削除
            print(message)
            splited = _message.rsplit("の", 1)
            splited.insert(1, "の")

            if splited[1].startswith("の"):
                start_rand = "".join(random.sample(splited[0], len(splited[0])))
                end_rand = "".join(random.sample(splited[2], len(splited[2])))

                result = start_rand + "の" + end_rand
                await message.channel.send(result)
    except IndexError:
        await message.channel.send("文字列がおかしいよ")
client.run(TOKEN)