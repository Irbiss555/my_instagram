from rest_framework import serializers
from instagram.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'image',
            'description',
            'liked_users',
            'likes_total',
            'comment_total',
        ]
        read_only_fields = [
            'user',
            'likes_total',
            'comment_total',
        ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'id',
            'post',
            'user'
        ]
