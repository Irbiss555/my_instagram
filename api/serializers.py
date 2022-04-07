from rest_framework import serializers
from instagram.models import Post, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'id',
            'post',
            'user'
        ]
        read_only_fields = ['user']


class PostSerializer(serializers.ModelSerializer):
    post_likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'image',
            'description',
            'post_likes',
            'liked_users',
            'likes_total',
            'comment_total',

        ]
        read_only_fields = [
            'user',
            'likes_total',
            'comment_total',
        ]
