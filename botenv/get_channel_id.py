from telethon import TelegramClient

api_id = 29388938
api_hash = '727879d8e834d1c00d1ea2a3f99237df'
client = TelegramClient('bot', api_id, api_hash)

async def get_channel_id():
    await client.start()
    # Замените 'your_channel_username' на @username вашего канала
    channel = await client.get_entity('@dishes')
    print(f"ID канала: {channel.id}")

with client:
    client.loop.run_until_complete(get_channel_id())
