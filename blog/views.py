
from django.shortcuts import render
import datetime
from django.http import HttpResponse, HttpResponseRedirect


def root(request):
    return HttpResponseRedirect('home')

def home_page(request):
    now = str(datetime.datetime.now())
    context = {'day': now}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
