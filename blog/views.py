
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Article


def root(request):
    return HttpResponseRedirect('home')

def home_page(request):
    context = {'articles': Article.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
