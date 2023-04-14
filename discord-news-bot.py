import discord
import json
import os
import time
import asyncio

# Create a discord Intents object
intents = discord.Intents.default()
# Add the specific intents that your bot will require
intents.members = True

# initialize a Discord client object
client = discord.Client(intents=intents)

# replace this with the ID of the Discord channel you want to send news updates to
news_channel_id = 1084229932038770708

# replace these with the paths to your news JSON files
news_files_path = ['wuxu-complete.json', 'wuxu-complete++.json']

# initialize a dictionary to hold the current news data for each file
news_data = {}

# function to read the news files and store their data in the news_data dictionary
def read_news_files():
    global news_data
    for file_path in news_files_path:
        with open(file_path, 'r') as f:
            news_data[file_path] = json.load(f)

# function to check for updates to the news data every 5 minutes
async def check_for_updates():
    global news_data
    while True:
        try:
            for file_path in news_files_path:
                # open the news file and load its contents into a dictionary
                with open(file_path, 'r') as f:
                    new_data = json.load(f)

                    # check if the news data has changed since the last time we checked
                    if new_data != news_data[file_path]:
                        # find any new news items that have been added or updated
                        new_news = []
                        for n in new_data['news']:
                            if n not in news_data[file_path]['news']:
                                new_news.append(n)
                            else:
                                for old_n in news_data[file_path]['news']:
                                    if n['id'] == old_n['id'] and n['date'] != old_n['date']:
                                        new_news.append(n)
                        if new_news:
                            # get the Discord channel object where we want to send news updates
                            news_channel = client.get_channel(news_channel_id)
                            for n in new_news:
                                # find the name of the app that has been updated
                                app_name = None
                                for app in new_data['apps']:
                                    if app['bundleIdentifier'] == n['appID']:
                                        app_name = app['name']
                                        break
                                # create a message to send to the Discord channel
                                message = f'{app_name} has been updated on {file_path}!'
                                # create an embed object with the news item details
                                embed = discord.Embed(title=n['title'], description=n['caption'], color=int(n['tintColor'], 16))
                                # set the image of the embed to the news item's imageURL
                                embed.set_image(url=n['imageURL'])
                                # send the message and embed to the Discord channel
                                await news_channel.send(message, embed=embed)
                        # update the stored news data with the new data
                        news_data[file_path] = new_data
        except Exception as e:
            # print any errors that occur while checking for updates
            print(f'Error checking for updates: {e}')
        # wait 5 minutes before checking for updates again
        await asyncio.sleep(300)

# log in the bot and start the update checking loop
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    read_news_files()
    client.loop.create_task(check_for_updates())

# start the bot by passing your Discord bot token to the client object
client.run('MTA5NjUxODk0MTkwOTcyMTIyOA.GVJq7L.99cAG8_Mzdl7wwWzlAnfd9hRcCIHtXwo_1EnnM')
