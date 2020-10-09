from django.http import HttpResponse
from kvak.functions.bot_updates import bot_updates, TG_URL
import requests


def bot_handler(request):
    updates_response = requests.post(TG_URL + 'getUpdates').json()
    if 'result' in updates_response and len(updates_response['result']):
        last_update_id = updates_response['result'][-1]['update_id']
        updates_response = requests.post(TG_URL + 'getUpdates', {'offset': last_update_id}).json()
        if 'result' in updates_response and len(updates_response['result']):
            bot_updates(updates_response['result'])
    return HttpResponse('success')
