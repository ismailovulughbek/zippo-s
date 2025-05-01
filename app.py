from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import logging
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import os

app = Flask(__name__)
CORS(app)

if not os.path.exists('logs'):
    os.makedirs('logs')

# logging.basicConfig(filename='logs/app.log',
#                     level=logging.INFO,
#                     format='%(asctime)s %(levelname)s %(message)s')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')
@app.route('/ser-human')
def ser_human():
    return render_template('ser-human.html')
@app.route('/ser-wellness')
def ser_wellness():
    return render_template('ser-wellness.html')
@app.route('/ser-laboratory')
def ser_laboratory():
    return render_template('ser-laboratory.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/intro_message', methods=['POST'])
def intro_message():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        service = data.get('service', '').strip()

        if not name or not email or not phone or not service:
            return jsonify({'status': 'error', 'message': 'Please fill in all fields!'}), 400


        text = f"📬 *NEW MESSAGE!*\n\n👤 Name: {name}\n📧 Email: {email}\n📞 Phone: {phone}\n🏥 Service: {service}"
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': text,
            'parse_mode': 'Markdown'
        }

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        response = requests.post(url, data=payload)
        
        if response.status_code != 200:
            return jsonify({'status': 'error', 'message': 'Could not send to Telegram!'}), 500

        return jsonify({'status': 'success', 'message': 'Message sent successfully'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Internal server error!'}), 500


@app.route('/contact_message', methods=['POST'])
def contact_message():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not phone or not subject or not message:
            return jsonify({'status': 'error', 'message': 'Please fill in all fields!'}), 400


        text = f"📬 *NEW MESSAGE!*\n\n👤 Name: {name}\n📧 Email: {email}\n📞 Phone: {phone}\n📌 Subject: {subject}\n\n📝 Message: {message}"
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': text,
            'parse_mode': 'Markdown'
        }

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        response = requests.post(url, data=payload)
        
        if response.status_code != 200:
            return jsonify({'status': 'error', 'message': 'Could not send to Telegram!'}), 500

        return jsonify({'status': 'success', 'message': 'Message sent successfully'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Internal server error!'}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
