import sys
import os

# Добавляем текущую директорию в sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import utils  # <--- Убедитесь, что этот импорт есть

from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object('config') # Загружаем конфигурацию из config.py


@app.route('/', methods=['GET'])
def index():
    """Отображает главную страницу с формой."""
    return render_template('index.html')


@app.route('/send_telegram', methods=['POST'])
def send_telegram():
    print("Request received at /send_telegram")  # Add this line
    print("Request form data:", request.form)  # Add this line
    try:
        name = request.form['name']
        phone = request.form['phone']

        message = f"Новая заявка с сайта!\n\nИмя: {name}\nТелефон: {phone}"

        if utils.send_telegram_message(message):  # Используем функцию из utils.py
            return redirect(request.referrer or url_for('index'))
        else:
            return jsonify({'status': 'error', 'message': 'Ошибка при отправке сообщения в Telegram!'}), 500

    except Exception as e:
        print(f"Ошибка: {e}")
        return jsonify({'status': 'error', 'message': f'Произошла ошибка: {str(e)}'}), 500

# ... (остальной код)


if __name__ == '__main__':
    app.run(debug=True)