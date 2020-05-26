from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView


class ArticleListView(ListView):
    model = Article
    template_name = "article/article_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list'] = Article.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/article_detail.html"