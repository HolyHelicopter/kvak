import requests
import random
import datetime
import time


TG_URL = "https://api.telegram.org/bot1221959365:AAHAZKkaa5hJF0bchJFfVM9uT9Hhv-jOfzg/"
BING_URL = "https://bing-image-search1.p.rapidapi.com/images/search?q="
BING_HEADERS = {
    "x-rapidapi-host": "bing-image-search1.p.rapidapi.com",
    "x-rapidapi-key": "fb3dd38f00msh738d9f9b25b29acp13d692jsn8859445253e3",
    "useQueryString": 'true'
}
BACKUP_QUERIES = [
    'лягушка мем',
    'лягушка косплей',
    'лягушка сказка',
    'лягушка нарисованная',
    'лягушка смешная',
    'лягушка кермит'
]


def bot_updates(updates):
    try:
        for update in updates:
            if 'message' in update:
                message = update['message']
                if 'text' in message and message['text']:
                    message_text = message['text']

                    lowercase_text = message_text.replace('К', 'к').replace('В', 'в').replace('А', 'а')

                    if 'квак' in lowercase_text:
                        words = message_text.split()

                        words_temp = []
                        for word in words:
                            if 'квак' not in word:
                                words_temp.append(word)
                        words = words_temp

                        query = 'лягушка'
                        for word in words:
                            query += ' ' + word

                        print(query)

                        found_images = requests.get(
                            BING_URL + query,
                            headers=BING_HEADERS
                        ).json()['value']

                        if not len(found_images):
                            print('no results')
                            backup_index = random.randint(0, len(BACKUP_QUERIES) - 1)
                            backup_query = BACKUP_QUERIES[backup_index]
                            print(backup_query)
                            found_images = requests.get(
                                BING_URL + backup_query,
                                headers=BING_HEADERS
                            ).json()['value']

                        if len(found_images):
                            image_index = random.randint(0, len(found_images) - 1)
                            image_url = found_images[image_index]['contentUrl']
                            try:
                                requests.post(
                                    TG_URL + 'sendPhoto',
                                    {
                                        'chat_id': '811288345',
                                        'photo': image_url
                                    }
                                )
                            except Exception as e:
                                print(str(e))
                                image_index = random.randint(0, len(found_images) - 1)
                                image_url = found_images[image_index]['contentUrl']
                                try:
                                    requests.post(
                                        TG_URL + 'sendPhoto',
                                        {
                                            'chat_id': '811288345',
                                            'photo': image_url
                                        }
                                    )
                                except Exception as e:
                                    pass

                            # file_content = requests.get(image_url)
                            # file_content = file_content.content
                            # data = {
                            #     'chat_id': '811288345',
                            # }
                            # requests.post(
                            #     "https://api.telegram.org/bot1221959365:AAHAZKkaa5hJF0bchJFfVM9uT9Hhv-jOfzg/sendPhoto",
                            #     data=data,
                            #     files={'photo': ('квак.jpg', file_content)}
                            # )
    except Exception as e:
        print(e)


current_time = datetime.datetime.now()
time_end = current_time + datetime.timedelta(hours=20)

updates_response = requests.post(TG_URL + 'getUpdates').json()
if 'result' in updates_response and len(updates_response['result']):
    last_update_id = updates_response['result'][-1]['update_id']
    offset = last_update_id

    while current_time < time_end:
        updates_response = requests.post(TG_URL + 'getUpdates', {'offset': offset}).json()
        if 'result' in updates_response and len(updates_response['result']):
            updates = updates_response['result']

            bot_updates(updates)

            last_update_id = updates[-1]['update_id']
            offset = last_update_id + 1

            time.sleep(10)

        current_time = datetime.datetime.now()
