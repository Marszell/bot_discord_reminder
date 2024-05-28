import discord
import asyncio
from resspon import handle_response
from reemendeer import check_reminders, add_reminder, list_reminders

intents = discord.Intents.default()
intents.messages = True  
intents.message_content = True 
intents.dm_messages = True  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(check_reminders(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await handle_response(message)
    
    if message.content.startswith('!reminder'):
        parts = message.content.split()
        if len(parts) >= 3:
            delay, context = parts[1], ' '.join(parts[2:])
            response = add_reminder(delay, context, message.author.id, message.channel.id, message.author.mention, message.guild is None)
            await message.channel.send(response)
        elif len(parts) == 2 and parts[1] == 'list':
            response = list_reminders(message.author.id)
            await message.channel.send(response)

client.run('YOUR_TOKEN')
