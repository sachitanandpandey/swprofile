from django.urls import path, include
from swprofile.views import *

from rest_framework.routers import DefaultRouter,SimpleRouter

router = DefaultRouter()
router.register('home', msg);
router.register('posts',postblog)

urlpatterns = [
    path('visha/', include(router.urls)),
]