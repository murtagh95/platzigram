from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    """Retorna un saludo"""
    return HttpResponse('Oh, hi! Current server time is {}'.format(
        datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sorted(request):
    """ Retorna un JSON con los números ordenados """
    # con GET obtenemos los parametros pasados por la url
    # estos se encuentran en un string
    print(request.GET.get('numbers'))
    numeros = request.GET.get('numbers').split(',')
    if len(numeros) > 0:
        numeros = [int(i) for i in numeros]
        numeros_ordenados = sorted(numeros)
        data = {
            'status': 'ok',
            'numbers': numeros_ordenados,
            'message': 'Interger sorted successfully.'
        }
    return HttpResponse(json.dumps(data, indent=4),
                        content_type='application/json')

def say_hi(request, name, age):
    """ Retorna un saludo """
    if age < 12:
        message = 'Sorry {}, you are not allowed here'
    else:
        message = 'Hello, {}! Welcome to Platzigram.'
    message = message.format(name)
    return HttpResponse(message)
