import openai

openai.api_key = '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'

async def check_translation_with_ai(original_text, translated_text):
    prompt = f"Исходный текст: {original_text}\nПеревод: {translated_text}\nОцените точность перевода. Правильно ли это переведено?"
    response = await openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()