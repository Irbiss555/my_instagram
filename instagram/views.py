from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    template_name = 'post_list.html'
    context_object_name = 'posts'
    model = Post
