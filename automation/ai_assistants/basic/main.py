import os
import json
import openai
import telebot

# === Конфигурация ===
TELEGRAM_TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("API_KEY")
TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")
openai.api_key = OPENAI_API_KEY

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# === Пути к картинкам ===
IMAGE_PATHS = {
    "1": "images/image1.png",
    "2": "images/image2.jpeg",
    "3": "images/image3.png"
}

# === Prompt для GPT ===
system_prompt = """
Ты — умный ассистент. На каждый пользовательский запрос ты возвращаешь JSON-объект следующего вида:

{
  "action": "<название_действия>",
  "params": { ... }
}

Вот доступные действия:
0. Для всех пользовательских запросов, которые не подчиняются сценариям ниже:
  {
    "action": "default",
  }

1. Показать заранее заготовленную картинку:
  {
    "action": "send_picture",
    "params": {
      "picture_key": "1"  // может быть "1", "2" или "3"
    }
  }

2. Отправить сообщение в заранее заданный Telegram-чат:
  {
    "action": "send_message",
    "params": {
      "text": "текст сообщения"
    }
  }

Описание картинок:
1 — Чёрный монолит на фоне скал. Выглядит загадочно и внушительно. Символизирует технологическое превосходство, непостижимую силу, инопланетность. Подходит для запросов вроде: «что-то загадочное», «технологичное», «монументальное», «инопланетное».
2 — Мем: «Жизнь у вас одна. Постарайтесь как можно больше работать. В раю работы нет». На фоне — снежная электроподстанция и грустный кот в форме Россети. Подходит для запросов про иронию, выгорание, офис, тяжёлую работу, сарказм.
3 — Чёрно-белый QR-код. Универсальный. Используется, если пользователь просит: «ссылка», «QR-код», «перейти по ссылке», «отсканировать».

Всегда возвращай только JSON. Никаких пояснений, никакого текста вне JSON.
"""

# === Обработка логики GPT ===
def get_action_from_gpt(user_message: str) -> dict | None:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    reply = response.choices[0].message.content.strip()

    try:
        return json.loads(reply)
    except json.JSONDecodeError as e:
        print("Ошибка JSON от GPT:", e)
        return None

# === Обработчики действий ===

def send_picture(chat_id, params):
    picture_key = params.get("picture_key", "1")
    image_path = IMAGE_PATHS.get(picture_key, IMAGE_PATHS["1"])

    with open(image_path, 'rb') as photo:
        bot.send_photo(chat_id, photo)

def send_message(chat_id, params):
    text = params.get("text", "")
    if text:
        bot.send_message(TARGET_CHAT_ID, text)
        bot.send_message(chat_id, "Сообщение отправлено!")
    else:
        bot.send_message(chat_id, "Текст сообщения не найден.")


# === Роутинг действий ===
ACTION_HANDLERS = {
    "send_picture": send_picture,
    "send_message": send_message,
}

# === Обработка входящих сообщений ===
@bot.message_handler(func=lambda message: message.chat.type == "private")
def handle_message(message):
    try:
        user_text = message.text
        action_payload = get_action_from_gpt(user_text)
        action = action_payload.get("action")
        params = action_payload.get("params", {})

        handler = ACTION_HANDLERS.get(action)
        handler(message.chat.id, params)

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "Я тебя не понял, переформулируй свой запрос пожалуйста.")

# === Запуск бота ===
if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
