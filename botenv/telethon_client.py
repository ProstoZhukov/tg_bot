from telethon import TelegramClient, events
from translation import translate_message_with_ai
from review import send_for_review
import asyncio

api_id = 29388938
api_hash = '727879d8e834d1c00d1ea2a3f99237df'
client = TelegramClient('bot', api_id, api_hash)

# Используйте ID английского канала, который вы хотите отслеживать
ENGLISH_CHANNEL = 1693929066  # Замените на полученный ID канала

# Флаг для отслеживания отправки последних 15 сообщений
sent_initial_messages = False

async def get_last_messages():
    # Получаем последние 15 сообщений из канала
    async for message in client.iter_messages(ENGLISH_CHANNEL, limit=15):
        original_message = message.message

        # Получение названия канала
        channel_entity = await client.get_entity(ENGLISH_CHANNEL)
        channel_name = channel_entity.title

        # Переводим сообщение через AI
        translated_message = await translate_message_with_ai(original_message)

        # Отправляем на проверку или публикуем напрямую
        await send_for_review(None, None, original_message, translated_message, channel_name)

@client.on(events.NewMessage(chats=ENGLISH_CHANNEL))
async def handler(event):
    global sent_initial_messages

    # Если последние 15 сообщений еще не были отправлены, отправляем их один раз
    if not sent_initial_messages:
        await get_last_messages()
        sent_initial_messages = True

    # Обработка нового сообщения
    original_message = event.message.message
    channel_name = event.chat.title

    # Переводим сообщение через AI с поддержкой разбиения на части
    translated_message = await translate_message_with_ai(original_message)

    # Отправляем на проверку
    await send_for_review(None, None, original_message, translated_message, channel_name)

async def start_telethon():
    # Подключаемся к клиенту
    await client.connect()
    if not client.is_user_authorized():
        print("Пожалуйста, авторизуйтесь с помощью client.start()")
        client.start()

    # Клиент остается подключенным
    await client.run_until_disconnected()

# Запускаем Telethon с помощью asyncio
if __name__ == '__main__':
    asyncio.run(start_telethon())
