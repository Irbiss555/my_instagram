from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from accounts.models import UserFollowing
from django.dispatch import receiver

from instagram.models import Post


@receiver(signal=post_save, sender=UserFollowing)
def add_user_following(sender, instance, created, **kwargs):
    if created:
        user1 = get_user_model().objects.get(pk=instance.user_id.id)
        user2 = get_user_model().objects.get(pk=instance.following_user_id.id)
        user1.profile.followings_total += 1
        user2.profile.followers_total += 1
        user1.profile.save()
        user2.profile.save()


@receiver(signal=post_save, sender=Post)
def add_user_post(sender, instance, created, **kwargs):
    if created:
        user = get_user_model().objects.get(pk=instance.user.id)
        user.profile.posts_total += 1
        user.profile.save()


@receiver(signal=post_delete, sender=Post)
def add_user_post(sender, instance, created, **kwargs):
    user = get_user_model().objects.get(pk=instance.user.id)
    user.profile.posts_total -= 1
    user.profile.save()
