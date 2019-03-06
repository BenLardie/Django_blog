
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Article, Comment


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

def create_comment(request):
    article = request.POST['article']
    comment = request.POST['new-comment']
    new_comment = Comment.objects.create(name=request.POST['name'],
                                         message=request.POST['new-comment'],
                                         Article=Article.objects.get(pk=request.POST['article'])
                                         )
    return HttpResponseRedirect('/articles/'+ request.POST['article'])
