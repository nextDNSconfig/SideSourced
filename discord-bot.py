import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.context import SlashContext
from discord_slash.model import SlashCommandOptionType
import os  # Added to access environment variables

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
slash = cog_ext.cog_slash(command_name="assign_roles")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_member_join(member):
    # Send the role assignment message when a new member joins
    await member.send("Welcome to the server! Please select your roles:")
    await assign_roles_message(member)

@slash.options(
    name="roles",
    description="Select roles",
    required=True,
    option_type=SlashCommandOptionType.STRING,
    choices=[
        {
            "name": "Role 1",
            "value": "role1"
        },
        {
            "name": "Role 2",
            "value": "role2"
        },
        # Add more role choices as needed
    ]
)
@slash.target(["bot"])
async def assign_roles(ctx: SlashContext, roles: str):
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name=roles)
    
    if role:
        await member.add_roles(role)
        await ctx.send(f"Assigned {roles} role to {member.display_name}")
    else:
        await ctx.send(f"Role {roles} not found")

async def assign_roles_message(member):
    # Send the role assignment message with the dropdown options
    await member.send(
        "Please select your roles:",
        components=[
            discord.ui.Select(
                placeholder="Select roles...",
                options=[
                    discord.SelectOption(label="Role 1", value="role1"),
                    discord.SelectOption(label="Role 2", value="role2"),
                    # Add more role options as needed
                ]
            )
        ]
    )

bot.run(os.getenv("DISCORD_TOKEN"))  # Retrieve the bot token from the environment variable
