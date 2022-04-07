from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import Profile, Gender, UserFollowing


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['avatar', 'about', 'phone', 'gender']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]


User = get_user_model()
admin.site.register(User, ProfileAdmin)
admin.site.register(Gender)
admin.site.register(UserFollowing)
