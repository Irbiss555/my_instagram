from django.urls import reverse
from django.views.generic import ListView, CreateView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    template_name = 'post_list.html'
    context_object_name = 'posts'
    model = Post


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_list')
