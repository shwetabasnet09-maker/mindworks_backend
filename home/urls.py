

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutSectionAPIView, HeroSectionViewSet, BannerStatListAPIView

router = DefaultRouter()
router.register("herosection", HeroSectionViewSet, basename="herosection")

urlpatterns = [
    path("", include(router.urls)),  # router URLs for HeroSection
    path("bannerstats/", BannerStatListAPIView.as_view(), name="bannerstats"),  
    path("about/", AboutSectionAPIView.as_view(), name="about-section"),
]
