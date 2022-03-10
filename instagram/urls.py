from django.urls import path

from instagram.views import (
    PostListView, PostCreateView,
    CommentCreateView, CommentDeleteView,
)

post_urls = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='post_create')
]

comment_urls = [
    path('post/<int:pk>/comment/create', CommentCreateView.as_view(), name='comment_create'),
    path('post/comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),
]


urlpatterns = post_urls
urlpatterns += comment_urls
