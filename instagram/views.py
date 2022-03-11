from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from instagram.forms import PostForm, CommentForm, LikeForm
from instagram.models import Post, Comment, Like


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


class PostDetailView(DetailView):
    template_name = 'instagram/post_detail.html'
    model = Post
    context_object_name = 'post'
    pk_url_kwarg = 'pk'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'instagram/post_detail.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.post = post
        comment.user = self.request.user
        comment.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('instagram:post_detail', kwargs={'pk': self.kwargs.get('pk')})


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        post = comment.post
        return reverse('instagram:post_detail', kwargs={'pk': post.pk})


class LikeAddView(CreateView):
    model = Like
    form_class = LikeForm
    template_name = 'instagram/post_list.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('instagram:post_list')

