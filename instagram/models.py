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

    def __str__(self):
        return self.text[:20]


class Like(models.Model):
    post = models.ForeignKey(
        to='instagram.Post', on_delete=models.CASCADE,
        related_name='likes', verbose_name='Лайк'
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        verbose_name='Пользователь', related_name='likes'
    )

    class Meta:
        unique_together = ['user', 'post']
