from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import (
    ServerViewSet
)

router = DefaultRouter(trailing_slash=True)
router.register('servers', ServerViewSet, 'server')

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^servers/?$', ServerViewSet.as_view(), name='servers'),
]
