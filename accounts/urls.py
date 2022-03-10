from django.urls import path

from django.contrib.auth.views import LogoutView

from accounts.views import (
    LoginUserView, RegisterView,
    ProfileView, UserListView,
)

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('list/', UserListView.as_view(), name='user_list'),
]
