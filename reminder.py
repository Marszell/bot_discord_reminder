import asyncio
from datetime import timedelta, datetime

reminders = []

async def check_reminders(client):
    while True:
        current_time = datetime.now()
        for reminder in reminders.copy():
            if reminder['time'] <= current_time:
                if reminder['dm']:
                    channel = await client.fetch_user(reminder['author_id'])
                else:
                    channel = client.get_channel(reminder['channel_id'])
                await channel.send(f"{reminder['mention']} Reminder: {reminder['context']}")
                reminders.remove(reminder)
        await asyncio.sleep(5)

def add_reminder(delay, context, author_id, channel_id, mention, dm):
    delay_amount, delay_unit = int(delay[:-1]), delay[-1]
    if delay_unit == 's':
        delay_seconds = delay_amount
    elif delay_unit == 'm':
        delay_seconds = delay_amount * 60
    elif delay_unit == 'h':
        delay_seconds = delay_amount * 3600
    else:
        return "Invalid time format!"
        
    remind_time = datetime.now() + timedelta(seconds=delay_seconds)
    reminders.append({
        'time': remind_time, 
        'context': context, 
        'author_id': author_id, 
        'channel_id': channel_id if not dm else None, 
        'mention': mention,
        'dm': dm
    })
    return f"Reminder set for {context} in {delay_amount}{delay_unit}"
    
def list_reminders(author_id):
    user_reminders = [r for r in reminders if r['author_id'] == author_id]
    if not user_reminders:
        return "You have no active reminders."
    else:
        response = "Your reminders:\n"
        for reminder in user_reminders:
            time_left = (reminder['time'] - datetime.now()).total_seconds()
            response += f"- {reminder['context']} in {int(time_left // 3600)}h {int((time_left % 3600) // 60)}m {int(time_left % 60)}s\n"
        return response
