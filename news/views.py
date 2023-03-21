from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def news(request):
    #return HttpResponse('<h1>Welcome to News Page</h1>')
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})

# Create your views here.
