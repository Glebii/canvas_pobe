from django.urls import path
from .views import ArticleListView, ArticleDetailView



urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list_of_articles'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path()
]