import discord
from discord.ext import commands
import os

# Get the bot token from the GitHub secret
TOKEN = os.environ['DISCORD_TOKEN']

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Define the role options that will be displayed in the dropdown menu
role_options = [
    {"name": "Role 1", "description": "Description for Role 1"},
    {"name": "Role 2", "description": "Description for Role 2"},
    # Add more role options as needed
]

# Function to create a role dropdown menu
async def create_role_dropdown(ctx):
    # Create a select menu with the role options
    select = discord.ui.Select(
        custom_id="role_selector",
        placeholder="Select a role",
        options=[
            discord.SelectOption(label=option["name"], description=option["description"])
            for option in role_options
        ],
    )

    # Create a view that contains the select menu
    view = discord.ui.View()
    view.add_item(select)

    # Send a message with the select menu
    await ctx.send("Select a role:", view=view)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to create the role dropdown menu
@bot.command()
async def roles(ctx):
    await create_role_dropdown(ctx)

# Event handler for handling role selection
@bot.event
async def on_dropdown(interaction):
    selected_option = interaction.data['values'][0]  # Get the selected option
    role_name = selected_option  # You can customize this based on how role names are stored

    # Find the role by name
    role = discord.utils.get(interaction.guild.roles, name=role_name)

    if role:
        member = interaction.user
        # Add the selected role to the member
        await member.add_roles(role)
        await interaction.response.send_message(f'You now have the {role.name} role!')
    else:
        await interaction.response.send_message("Role not found.")

# Start the bot
bot.run(TOKEN)
