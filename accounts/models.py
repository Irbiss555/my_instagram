from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


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
    followings = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')
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
