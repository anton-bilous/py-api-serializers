from django.urls import path, include
from rest_framework import routers

from .views import GenreViewSet, ActorViewSet


app_name = "cinema"

router = routers.SimpleRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
