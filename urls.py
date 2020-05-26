from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:key>/detail/', views.post_detail, name='post_detail'),
    path('<int:key>/update/', views.post_update, name='post_update'),
    path('create/', views.post_create, name='post_create'),
    path('<int:key>/delete', views.post_delete, name='post_delete')
]