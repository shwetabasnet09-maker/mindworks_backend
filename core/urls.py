from rest_framework.routers import DefaultRouter
from .views import  ProductViewSet, ServiceViewSet

router = DefaultRouter()
router.register("products", ProductViewSet)


router.register("services", ServiceViewSet, basename="services")


urlpatterns = router.urls
