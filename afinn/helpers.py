import re
import math

AFINN_VERSION = 'AFINN-111.txt'

from django.conf import settings

def get_afinn():
    afinn = dict(map(lambda (w, s): (w, int(s)), [ 
                ws.strip().split('\t') for ws in open('%s/%s' % (settings.AFINN_ROOT, AFINN_VERSION)) ]))

    return afinn

def get_sentiment(text):
    # Word splitter pattern
    afinn = get_afinn()

    pattern_split = re.compile(r"\W+")

    """
    Returns a float for sentiment strength based on the input text.
    Positive values are positive valence, negative value are negative valence. 
    """
    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        # How should you weight the individual word sentiments? 
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
        
    else:
        sentiment = 0
    return sentiment
