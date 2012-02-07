from django.shortcuts import render_to_response
from afinn.helpers import get_sentiment

def sentiment():
    text = request.GET.get('text') or request.POST.get('text')
    return HttpResponse(get_sentiment(text))
