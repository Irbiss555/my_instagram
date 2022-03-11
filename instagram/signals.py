from django.db.models.signals import post_save, post_delete
from instagram.models import Like, Post
from django.dispatch import receiver


@receiver(signal=post_save, sender=Like)
def add_like_post(sender, instance, created, **kwargs):
    if created:
        post = Post.objects.get(pk=instance.post.id)
        post.likes_total += 1
        post.save()
