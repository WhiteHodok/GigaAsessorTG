import openai
import telebot

# установка ключа API для OpenAI
openai.api_key = ""

# создание объекта бота
bot = telebot.TeleBot(token='')

# обработчик сообщений
@bot.message_handler(func=lambda message: True)
def process_message(message: telebot.types.Message):
    # определение ключевого слова для разделения предпромпта и промпта
    keyword = '//'
    # добавление постоянного предпромпта
    prompt_prefix = "Понятен ли тебе мой промпт(не твой, а мой)? Дай ему оценку(моему промпту). Что мне надо в нём исправить(укажи так, чтобы было понятно тебе), чтобы тебе было понятно, что я хочу(не ты хочешь, а я), может надо что-то уточнить(для темы промпта)?\n//"
    # разделение сообщения на предпромпт и промпт
    input_text = message.text
    full_prompt = prompt_prefix + input_text  # склеить предпромпт и промпт
    # отправка запроса в API OpenAI
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=full_prompt,
        max_tokens=1024,
        temperature=0.5
    )
    # обработка ответа от ChatGPT 3.5
    output_text = response.choices[0].text
    # отправка ответа пользователю в Telegram
    bot.send_message(chat_id=message.chat.id, text=output_text)

# запуск бота
bot.polling(none_stop=True)
