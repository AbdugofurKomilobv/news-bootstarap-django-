from django.shortcuts import render

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