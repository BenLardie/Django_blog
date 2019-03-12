
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Article, Comment
from blog.forms import ArticleForm
from blog.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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



def new_article(request):
    new_form = ArticleForm()
    context = {'form': new_form}
    response = render(request, 'newarticle.html', context)
    return HttpResponse(response)

@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect('/articles/' +str(form.pk))
        else:
            print(form.errors)
    else:
        form = ArticleForm()
    return render(request, 'newarticle.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()
    context = {'form': form}
    response = render(request, 'login.html', context)
    return HttpResponse(response)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home/')
    else:
        form = UserCreationForm()
    html_response = render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)


@login_required
def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
        context = {'form': form, 'article': article}
        return render(request, 'edit.html', context)

    elif request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            updated_article = form.save()
            return HttpResponseRedirect('/articles/' + str(article.id))
        else:
            context = {'form': form, 'article': article}
            response = render(request, 'edit.html', context)
            return HttpResponse(response)
