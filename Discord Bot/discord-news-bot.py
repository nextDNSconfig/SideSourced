import os
import shutil
import json
import discord
from discord.ext import commands
from discord import Embed

# Specify the channel ID where the bot will send announcements
CHANNEL_ID = 1084229932038770708

# Initialize the Discord bot with intents
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a function to read the JSON file and return its contents as a dictionary
def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Define a function to write the dictionary to a new JSON file with a specified name
def write_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Define a function to compare two JSON dictionaries and return True if they are different
def compare_json(old_data, new_data):
    return old_data != new_data

# Define a function to check for updates to the 'news' section in the JSON file
async def check_updates():
    # Read the old JSON file
    old_data = read_json_file('/Discord Bot/wuxu-complete-old.json')
    # Read the new JSON file
    new_data = read_json_file('/wuxu-complete.json')
    # Compare the old and new JSON files
    if compare_json(old_data, new_data):
        # Check if there are any updates to the 'news' section
        for old_news in old_data['news']:
            for new_news in new_data['news']:
                if old_news['identifier'] == new_news['identifier']:
                    if old_news['date'] != new_news['date']:
                        # Delete the old JSON file
                        os.remove('wuxu-complete-old.json')
                        shutil.copy('wuxu-complete.json','wuxu-complete-old.json')
                        # Send an announcement in the specified Discord channel with an embedded image
                        app_id = new_news['appID']
                        for app in new_data['apps']:
                            if app['bundleIdentifier'] == app_id:
                                title = f"Added {app['name']} to WuXu's Library!" if old_news['date'] is None else f"Updated {app['name']} on WuXu's Library!"
                                embed = Embed(title=title, description=new_news['caption'], color=int(new_news['tintColor'], 16))
                                embed.set_image(url=new_news['imageURL'])
                                embed.add_field(name="Browse WuXu's Library", value="[Click here](https://bit.ly/wuxuslibrary-browse)", inline=False)
                                await bot.get_channel(CHANNEL_ID).send(embed=embed)
                        return
        # Write the new JSON data to the old JSON file
        write_json_file(new_data, 'wuxu-complete-old.json')

# Define a command for the bot to manually check for updates
@bot.command()
async def check(ctx):
    await check_updates()

# Define a background task to continuously check for updates to the JSON file
@bot.event
async def on_ready():
    print('Bot is ready')
    bot.loop.create_task(check_updates())

# Start the bot with the specified Discord bot token
bot.run('MTA5NjUxODk0MTkwOTcyMTIyOA.G8fPLn.r4NTFdJVt3Ip6c-DWcQU2HQdcPxFMmc5grLf1g')
