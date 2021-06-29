from django.shortcuts import render

from django.http import HttpResponse
from posts.helpers import posts_helpers

JSON = {
    'posts': [{
        'id': 1,
        'title': 'Django',
        'body': 'Learning'
    },
    {
        'id': 2,
        'title': 'Other',
        'body': 'Post'
    },
    {
        'id': 3,
        'title': '3rd',
        'body': 'Post'
    }]
}
        
# Create your views here.
def get(request):
    return HttpResponse(f'{JSON}')


def show(request, id):
    response = posts_helpers.get_by_id(JSON, id)
    return HttpResponse(f'{response}', content_type='application/json')