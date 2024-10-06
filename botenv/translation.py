import openai
import textwrap

openai.api_key = ''

# Максимум токенов, которые мы можем отправить за один запрос
MAX_TOKENS = 1500  # Учтем запас на модельные токены


# Функция для разбиения текста на блоки
def split_text(text, max_tokens):
    # Ограничим количество символов, основываясь на оценке, что 1 токен ≈ 4 символа
    approx_max_chars = max_tokens * 4  # Это приблизительное число символов, которые соответствуют количеству токенов
    return textwrap.wrap(text, approx_max_chars)


# Функция для перевода с помощью OpenAI
def translate_message_with_ai(message):
    chunks = split_text(message, MAX_TOKENS)
    translated_chunks = []

    for chunk in chunks:
        prompt = f"Переведи этот текст с английского на русский: {chunk}"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=MAX_TOKENS
        )
        translated_chunk = response.choices[0].text.strip()
        translated_chunks.append(translated_chunk)

    # Объединяем переведенные части в один текст
    return ' '.join(translated_chunks)