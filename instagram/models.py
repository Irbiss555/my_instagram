from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to='post_pics', null=True, blank=True, verbose_name='Image')
    description = models.TextField(max_length=3000, blank=True, null=True)
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='posts'
    )
    liked_users = models.ManyToManyField(
        to=get_user_model(),
        related_name='liked_posts',
        through='instagram.Like',
        through_fields=('post', 'user'),
        blank=True
    )
    likes_total = models.IntegerField(
        default=0,
        blank=True,
        validators=(MinValueValidator(0),)
    )
    comment_total = models.IntegerField(
        default=0,
        blank=True,
        validators=(MinValueValidator(0),)
    )

    def __str__(self):
        return f'{self.user} {self.description}'


class Comment(models.Model):
    post = models.ForeignKey(
        to='instagram.Post', on_delete=models.CASCADE,
        related_name='comments', verbose_name='Пост'
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='comments'
    )
    text = models.TextField(
        max_length=400, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return self.text[:20]


class Like(models.Model):
    post = models.ForeignKey(
        to='instagram.Post', on_delete=models.CASCADE,
        related_name='post_likes', verbose_name='Пост'
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='user_likes'
    )

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return f'{self.user} likes post "{self.post}"'
