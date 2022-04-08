from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated
from rest_framework.views import APIView

from api.permissions import IsUserOwner, DenyAny
from instagram.models import Post, Like
from api.serializers import PostSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsUserOwner()]
        return super().get_permissions()


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [DenyAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        elif self.request.method in ['POST', 'DELETE']:
            return [IsAuthenticated(), IsUserOwner()]
        return super().get_permissions()


class LikeAPIView(APIView):
    post_obj = None
    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        likes = self.post_obj.post_likes.all()
        serializer = LikeSerializer(likes, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        if self.request.user in self.post_obj.liked_users.all():
            self.remove_like()
        else:
            self.add_like()
        response = {'likes_total': self.post_obj.liked_users.count()}
        return JsonResponse(response, safe=False)

    def remove_like(self):
        like = Like.objects.get(user=self.request.user, post=self.post_obj)
        like.delete()

    def add_like(self):
        Like.objects.create(user=self.request.user, post=self.post_obj)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()
