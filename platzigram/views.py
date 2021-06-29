from django.http import HttpResponse, response


from datetime import datetime
from django.http import JsonResponse
import json

def hello_world(request):
    """
    Example for function un Django in views module
    """
    now = datetime.now().strftime('%Y-%m-%d %H:%M hrs')
    return HttpResponse(f'Current server time is: {now}')

def hi(request):
    """
    Using the HttpResponse and the JsonResponse
    """
    numbers = request.GET['numbers'].split(',')
    numbers = sorted([int(i) for i in numbers])

    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Sorted ok'
    }

    data = json.dumps(data, indent=4)

    return HttpResponse(data, content_type='application/json')
    