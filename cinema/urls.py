from django.urls import path, include
from rest_framework import routers

from .views import GenreViewSet, ActorViewSet, CinemaHallViewSet, MovieViewSet


app_name = "cinema"

router = routers.SimpleRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
