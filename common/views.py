from django.shortcuts import redirect, render

from common.forms import NewsForm
from django.middleware.csrf import get_token
from .models import *


def index(request):
    news = News.objects.all()
    categories = Categories.objects.all()

    context = {
        "news": news,
        "categories": categories
    }
    return render(request=request,template_name='index.html',context=context)

def categories(request,category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Categories.objects.all()

    context = {
        "news": news,
        "categories": categories
    }
    return render(request=request,template_name='categories.html',context=context)

def new_about(request,new_id):
    new = News.objects.get(pk=new_id)
    

    context = {
        "new": new
    }

    return render(request=request,template_name='new_about.html',context=context)



def add_news(request):
    print("token = =",get_token(request))
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            news.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request=request,template_name='add_new.html',context={'form':form})