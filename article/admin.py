from django.contrib import admin
from .models import ArticleCategory, Article, ArticleImage


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
   
 

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name','text', 'price', 'phone', 'category']
    list_filter = ['name', 'price', 'category']
    list_editable = ['price', 'text']
    


class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'article']
   

 
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleImage, ArticleImageAdmin)