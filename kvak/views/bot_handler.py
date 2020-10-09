from django.http import HttpResponse


def bot_handler(request):
    return HttpResponse('it works')
