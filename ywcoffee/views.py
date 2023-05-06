from django.shortcuts import render

from django.http import HttpResponse
import random
from django.template.loader import render_to_string
from django.shortcuts import redirect
from ywcoffee.models import Article

def home_view(request):

    number = random.randint(1, 3)

    article_obj = Article.objects.get(id=number)
    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    HTML_STRING = f"""
    <h1>{article_obj.title} - {article_obj.id}</h1>
    <p>{article_obj.content}!</p>
    """.format(**context)
    return HttpResponse(HTML_STRING)

def site_view(request):
    
    #response = redirect("index.html")
    #return response
    #HTML_STRING1 = render_to_string("index.html")
    #return HttpResponse(HTML_STRING1)
    return render(request, 'index.html')

def coffee_view(request):
    HTML_STRING2 = render_to_string("coffees.html")
    return HttpResponse(HTML_STRING2)

