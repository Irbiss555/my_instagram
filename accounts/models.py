from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    followings = models.ManyToManyField(
        to='self',
        related_name='followers',
        through='accounts.UserFollowing',
        symmetrical=False,
        blank=True
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Profile(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        blank=False,
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    avatar = models.ImageField(upload_to='user_pics', blank=False, verbose_name='Avatar')
    about = models.TextField(max_length=2500, blank=True, verbose_name='About')
    phone = models.CharField(max_length=50, blank=True, verbose_name='Phone')
    gender = models.ForeignKey(
        to='accounts.Gender',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Gender'
    )
    followers_total = models.IntegerField(
        default=0,
        blank=True,
        validators=(MinValueValidator(0),)
    )
    followings_total = models.IntegerField(
        default=0,
        blank=True,
        validators=(MinValueValidator(0),)
    )
    posts_total = models.IntegerField(
        default=0,
        blank=True,
        validators=(MinValueValidator(0),)
    )

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Gender(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')

    def __str__(self):
        return f'{self.pk}. {self.name}'


class UserFollowing(models.Model):
    user_id = models.ForeignKey(get_user_model(), related_name='user_following', on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(get_user_model(), related_name='user_followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'following_user_id')

    def __str__(self):
        return f'User ID={self.user_id} followed to user ID={self.following_user_id}'
