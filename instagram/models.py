from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to='post_pics', null=True, blank=True, verbose_name='Image')
    description = models.TextField(max_length=3000, blank=True, null=True)
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