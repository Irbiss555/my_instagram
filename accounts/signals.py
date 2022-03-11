from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from accounts.models import UserFollowing
from django.dispatch import receiver


@receiver(signal=post_save, sender=UserFollowing)
def add_user_following(sender, instance, created, **kwargs):
    if created:
        user1 = get_user_model().objects.get(pk=instance.user_id.id)
        user2 = get_user_model().objects.get(pk=instance.following_user_id.id)
        user1.profile.followings_total += 1
        user2.profile.followers_total += 1
        user1.profile.save()
        user2.profile.save()
