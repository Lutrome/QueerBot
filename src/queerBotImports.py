# Pull Discord Client ID, Client Secret, and Bot Token from discordKeys.py
from keys.discordKeys import *

# Library Imports
import discord as dpy # Discord.py Library (v1.4.0a)
import discord.ext.commands as discordExtCmds # Discord.py Commands Extension
import discord.ext.tasks as discordExtTasks # Discord.py Tasks Extension
import boto3 # Boto3 API for Amazon Web Services (v1.13.11)
import asyncio # Asynchronous Input/Output (Python Built-In)