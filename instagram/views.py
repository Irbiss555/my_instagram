from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    template_name = 'instagram/post_list.html'
    context_object_name = 'posts'
    model = Post


class PostCreateView(CreateView):
    template_name = 'instagram/post_create.html'
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('instagram:post_list')


class CommentCreateView(CreateView):
    pass


class CommentDeleteView(DeleteView):
    pass
