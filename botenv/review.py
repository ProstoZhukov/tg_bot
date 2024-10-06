from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from ai_check import check_translation_with_ai


# Отправка сообщения на проверку
async def send_for_review(update, context, original_text, translated_text, channel_name):
    keyboard = [
        [InlineKeyboardButton("Отправить", callback_data='approve')],
        [InlineKeyboardButton("Отклонить", callback_data='cancel')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправка оригинала и перевода с указанием канала
    message = f"Канал: {channel_name}\n\nОригинал:\n{original_text}\n\nПеревод:\n{translated_text}"
    ai_feedback = await check_translation_with_ai(original_text, translated_text)
    await context.bot.send_message(chat_id=405771190, text=f"{message}\n\nAI проверка:\n{ai_feedback}",
                             reply_markup=reply_markup)


# Обработка нажатий кнопок
async def button_handler(update, context):
    query = update.callback_query

    # Если нажата кнопка "Отправить"
    if query.data == 'approve':
        await context.bot.send_message(chat_id=2441605067, text=query.message.text)
        await query.edit_message_text(text="Сообщение отправлено в канал.")

    # Если нажата кнопка "Отклонить"
    elif query.data == 'cancel':
        await query.edit_message_text(text="Сообщение отклонено.")