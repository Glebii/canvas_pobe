from django.db import models
from django.conf import settings
from django.utils import timezone


class ArticleCategory(models.Model):
    name = models.CharField(verbose_name='Названия категорий', max_length=64, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(verbose_name='Название работы', max_length=128, blank=True, null=True)
    text = models.TextField(verbose_name='Описание работы', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Цена', blank=True, null=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=16, blank=True, null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, verbose_name='Категории', blank=True, null=True)


class ArticleImage(models.Model):
    image = models.ImageField(verbose_name='Фотографии', upload_to='articleimage/', blank=True, null=True,)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Объявление',blank=True, null=True)


