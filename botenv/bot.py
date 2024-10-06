from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from review import button_handler
from telethon_client import start_telethon
import asyncio

# Функция для старта бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Команда /start получена")
    await update.message.reply_text('Привет! Я бот для перевода и проверки сообщений.')


async def main() -> None:
    # Создание приложения с использованием ApplicationBuilder
    application = ApplicationBuilder().token("7443502140:AAEqGGDJDH_92jVkaknGJ80cblsLCx2Harc").build()

    # Команда /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик inline-кнопок
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запуск Telethon для обработки сообщений в виде асинхронной задачи
    telethon_task = asyncio.create_task(start_telethon())

    # Запуск long-polling для Telegram бота
    try:
        await application.run_polling()
    finally:
        # Ожидаем завершения задачи Telethon при остановке приложения Telegram
        await telethon_task


if __name__ == '__main__':
    # Запуск основного потока в существующем цикле событий
    asyncio.run(main())
