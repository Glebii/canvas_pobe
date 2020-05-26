from article.models import Article
from django.views.generic import ListView 

class IndexPage(ListView):
    model = Article 
    template_name = 'article/index.html'