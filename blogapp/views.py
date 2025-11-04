from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm

class BlogView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = "Posts/blogView.html"


class BlogCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "Posts/blogCreate.html"
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "Posts/blogUpdate.html"
    success_url = reverse_lazy('blog_list')


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "Posts/blogDelete.html"
    success_url = reverse_lazy('blog_list')

