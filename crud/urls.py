from django.urls import include, path
from rest_framework import routers

from .views import TeamViewSet, SportViewSet, ProductViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet, basename="teams")
router.register(r'sports', SportViewSet, basename="sports")
router.register(r'products', ProductViewSet, basename="products")
router.register(r'customer', CustomerViewSet, basename="customers")

urlpatterns = [
    path('', include(router.urls)),
]
