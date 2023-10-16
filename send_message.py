import requests


token = '6337007667:AAFQqUfjNHkVyLfrHrUO2spi1B6OZl9-7wk'
chat_id = '-4070570430'
text = 'test2'


def send_in_telegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text
    }

    req = requests.post(method, data)


send_in_telegram()