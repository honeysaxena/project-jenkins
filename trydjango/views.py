from django.http import HttpResponse
import random

def home_view(request):

    name = "Justin"
    number = random.randint(10, 127685373)
    HTML_STRING = f"""
    <h1>Hello {name} - {number}</h1>
    """
    return HttpResponse(HTML_STRING)