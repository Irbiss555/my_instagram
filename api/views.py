from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated

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
