import discord
from discord.ext import commands
import asyncio
import pytz
import os

client = discord.Client()

token = "ODY0Nzk2MTQ4ODkwOTkyNjUw.YO6qLQ.YKuXHNMfS75STEhk2DBJzxQyI6M"

@client.event
async def on_ready():

    print(client.user.id) 
    print(client.user.name)
    print('성공적으로 봇을 작동시켰습니다.')
    game = discord.Game("자세한 명령어가 궁금하시다면 %명령어를 입력해주세요!") 
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "리듬 명령어":
        embed = discord.Embed(colour=discord.Colour.blue(), title="📋명령어 목록📋",description="```리듬봇 명령어``` !play (바로 재생하기), !search (노래 검색하기), !pause (현재 재생노래 일시 중지하기), !np (현재 재생중인 노래 표시하기), !skip (다음 노래로 건너뛰기), !seek (현재 재생중인 노래 탐색하기), !loopqueue (노래 전체 계속 반복하기), !loop (현재 재생중인 노래 반복하기), !volume (봇의 음량 조절하기), !rewind (되감기), !shuffle (노래 랜덤형식으로 듣기), !lyrics (현재 노래 가사 보기)") 
        await message.channel.send(embed=embed)

    if message.content == "리듬명령어":
        embed = discord.Embed(colour=discord.Colour.blue(), title="📋명령어 목록📋",description="```리듬봇 명령어``` !play (바로 재생하기), !search (노래 검색하기), !pause (현재 재생노래 일시 중지하기), !np (현재 재생중인 노래 표시하기), !skip (다음 노래로 건너뛰기), !seek (현재 재생중인 노래 탐색하기), !loopqueue (노래 전체 계속 반복하기), !loop (현재 재생중인 노래 반복하기), !volume (봇의 음량 조절하기), !rewind (되감기), !shuffle (노래 랜덤형식으로 듣기), !lyrics (현재 노래 가사 보기)") 
        await message.channel.send(embed=embed)

    if message.content == "히드라 명령어":
        embed = discord.Embed(colour=discord.Colour.blue(), title="📋명령어 목록📋",description="```히드라봇 명령어``` .help (도움말), .lyrics (현재 재생중인 노래 가사보기 ), .lyrics [노래제목] (선택한 노래 제목 보기), .ping (봇의 지연시간 표시), .play [노래제목/url] (입력한 음악 재생), .search [노래제목] (노래를 검색하고 선택), .voteskip (현재 트랙을 건너뛰도록 투표), .skip (현재 음악 스킵)") 
        await message.channel.send(embed=embed)

    if message.content == "히드라명령어":
        embed = discord.Embed(colour=discord.Colour.blue(), title="📋명령어 목록📋",description="```히드라봇 명령어``` .help (도움말), .lyrics (현재 재생중인 노래 가사보기 ), .lyrics [노래제목] (선택한 노래 제목 보기), .ping (봇의 지연시간 표시), .play [노래제목/url] (입력한 음악 재생), .search [노래제목] (노래를 검색하고 선택), .voteskip (현재 트랙을 건너뛰도록 투표), .skip (현재 음악 스킵)") 
        await message.channel.send(embed=embed)

client.run(token)