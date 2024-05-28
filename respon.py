import random

async def handle_response(message):
    message_content = message.content.lower()

    if message_content == 'hallo':
        await message.channel.send('hallo juga :)')
        return
    if message_content == 'motivasi':
        await message.channel.send('Semangat yahh :)')
        return
    if message_content == 'help':
        await message.channel.send('ada yang bisa dibantu ?')
        return
    if message_content == 'roll':
        await message.channel.send(str(random.randint(1,6)))
        return
