from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from todobucket.api.views import BucketViewSet, TodoViewSet

router = routers.DefaultRouter()
router.register('bucket', BucketViewSet)
router.register('Todo', TodoViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
