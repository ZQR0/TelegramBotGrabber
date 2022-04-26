from telethon import TelegramClient, events
from grabber_config import *

#Client defination
client = TelegramClient('Grabber', api_id, api_hash, retry_delay=3)


@client.on(events.NewMessage(chats=channels_id))
async def my_event_handler(event):

    if (event.message):
        await client.send_message(my_channel_id, event.message)

#Starting client
client.start()
client.run_until_disconnected()
