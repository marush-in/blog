from django.urls import path
from .import views

app_name = 'blog'


urlpatterns = [
    path('',),
    path('posts/<slug>',),
    path('category/<slug>',),
]
