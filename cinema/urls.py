from django.urls import path, include
from rest_framework import routers

from .views import GenreViewSet


app_name = "cinema"

router = routers.SimpleRouter()
router.register("genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
