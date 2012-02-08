from django.http import HttpResponse
from afinn.helpers import get_sentiment

def sentiment():
    text = request.GET.get('text') or request.POST.get('text')
    return HttpResponse(get_sentiment(text))
