from django.urls import path
from django.conf.urls import include

from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,)

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')


urlpatterns = [
    path('', include(router.urls),),
    path('group/', GroupViewSet.as_view(), name='group'),
    path('follow/', FollowViewSet.as_view(), name='follow'),
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
