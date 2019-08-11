from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Category


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=True).order_by('-created_at')
    paginate_by = 12
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostListByCategoryView(ListView):
    model = Post
    paginate_by = 12
    context_object_name = 'posts'
    template_name = 'blog/post_category.html'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Post.objects.order_by('-created_at').filter(
            category=category
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category, slug=self.kwargs['slug']
        )
        return context
