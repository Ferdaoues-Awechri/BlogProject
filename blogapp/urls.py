from django.urls import path
from .views import BlogView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
