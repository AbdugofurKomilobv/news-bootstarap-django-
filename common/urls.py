
from django.urls import path

from .views import *

urlpatterns = [

path('',index,name='home'),
path('categories/<int:category_id>/',categories,name='cat'),
path('new_about/<int:new_id>/',new_about,name='new_about'),
path('add_news',add_news,name='add_news')


]