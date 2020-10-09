from django.http import HttpResponse
import requests
import json


def bot_handler(request):
    message = json.dumps(request.POST)

    print('https://b24-tmfi1y.bitrix24.ru/rest/1/p12anzljw63jx12z/im.notify/?to=1&message=' + message)

    resp = requests.get(
        "https://bing-image-search1.p.rapidapi.com/images/search?q=жаба",
        headers={
            "x-rapidapi-host": "bing-image-search1.p.rapidapi.com",
            "x-rapidapi-key": "fb3dd38f00msh738d9f9b25b29acp13d692jsn8859445253e3",
            "useQueryString": 'true'
        }
    ).json()
    # resp['value'][12]['contentUrl']

    requests.post(
        'https://api.telegram.org/bot1221959365:AAHAZKkaa5hJF0bchJFfVM9uT9Hhv-jOfzg/sendMessage',
        {
            'chat_id': '811288345',
            'text': 'this is a message'
        }
    )

    return HttpResponse('success')

    file_link = ''

    file_content = requests.get(file_link)
    file_content = file_content.content
    data = {
        'chat_id': '811288345',
    }
    requests.post(
        "https://api.telegram.org/bot1221959365:AAHAZKkaa5hJF0bchJFfVM9uT9Hhv-jOfzg/sendPhoto",
        data=data,
        files={'photo': ('квак.jpg', file_content)}
    )

    return HttpResponse('it works')
