from django.db.models.signals import post_save, post_delete
from instagram.models import Like, Post, Comment
from django.dispatch import receiver


@receiver(signal=post_save, sender=Like)
def add_like_post(sender, instance, created, **kwargs):
    if created:
        post = Post.objects.get(pk=instance.post.id)
        post.likes_total += 1
        post.save()


@receiver(signal=post_save, sender=Comment)
def add_comment(sender, instance, created, **kwargs):
    if created:
        post = Post.objects.get(pk=instance.post.id)
        post.comment_total += 1
        post.save()
