from django.urls import path

from django.contrib.auth.views import LogoutView

from accounts.views import (
    LoginUserView, index_view, RegisterView
)

app_name = 'accounts'

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
]
