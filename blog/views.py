
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Article


def root(request):
    return HttpResponseRedirect('home')

def home_page(request):
    context = {'articles': Article.objects.filter(draft = False).order_by('published_date').all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def open_blog(request, id):
    article = Article.objects.get(pk=id)
    context = {'article': article}
    response = render(request, 'article.html', context)
    return HttpResponse(response)
