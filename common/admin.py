from django.contrib import admin


from .models import *

class NewCat(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(Categories,NewCat)


class NewNew(admin.ModelAdmin):
    list_display = ('title','context','created_ed','updated_ed','category','photo')
    search_fields = ('title',)


admin.site.register(News,NewNew)

