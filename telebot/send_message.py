import requests
from .models import TelebotSettings

# token = '6337007667:AAFQqUfjNHkVyLfrHrUO2spi1B6OZl9-7wk'
# chat_id = '-4070570430'
# text = 'test2'


def send_in_telegram(tg_name, tg_phone):
    if TelebotSettings.objects.get(pk=1):
        settings = TelebotSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        a = text.find('{')
        b = text.find('}')
        c = text.rfind('{')
        d = text.rfind('}')

        if a and b and c and d:
            part_1 = text[0:a]
            part_2 = text[b+1:c]
            part_3 = text[d:-1]

            text_slise = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slise = text

        try:
            data = {
                'chat_id': chat_id,
                'text': text_slise
            }
            req = requests.post(method, data)

        except:
            pass

        finally:
            if req.status_code != 200:
                print('Request Error!')
            elif req.status_code == 500:
                print('Server Error 500!')
            else:
                print('Everything Ok, request was send!')

    else:
        pass
