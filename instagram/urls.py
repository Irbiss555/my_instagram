from django.urls import path

from instagram.views import (
    PostListView, PostCreateView,
    CommentCreateView, CommentDeleteView,
    PostDetailView, LikeAddView,
)

app_name = 'instagram'

post_urls = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]

comment_urls = [
    path('post/<int:pk>/comment/create', CommentCreateView.as_view(), name='comment_create'),
    path('post/comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),
]

like_urls = [
    path('post/<int:pk>/like/add', LikeAddView.as_view(), name='like_add'),
]

urlpatterns = post_urls
urlpatterns += comment_urls
urlpatterns += like_urls
