from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FoodsViewSet, FoodViewSet

router = DefaultRouter()
router.register(r"foods", FoodsViewSet)
router.register(r"food", FoodViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
