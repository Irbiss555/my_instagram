from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'likes', views.LikeViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_auth_token, name='api_token_auth')
]
