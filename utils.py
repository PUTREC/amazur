import sys
import os

# Добавляем текущую директорию в sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config  # Теперь это должен быть абсолютный импорт
import requests

def send_telegram_message(message):
    """Отправляет сообщение в Telegram."""
    bot_token = config.BOT_TOKEN
    chat_id = config.CHAT_ID

    print(f"BOT_TOKEN: {bot_token}")  # Add this line
    print(f"CHAT_ID: {chat_id}")  # Add this line
    print(f"Message: {message}") 

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    print(f"Payload: {payload}")  # Add this line
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        print(f"Telegram API response: {response.json()}")  # Add this line
        return True
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке в Telegram: {e}")
        return False