from django.urls import path
from .views import PostListView, PostDetailView, PostListByCategoryView

app_name = 'blog'


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('posts/<slug>', PostDetailView.as_view(), name='detail'),
    path('category/<slug>', PostListByCategoryView.as_view(), name='category'),
]
