
from django.urls import path
from .views import HomePageAPIView

urlpatterns = [
    path("home/", HomePageAPIView.as_view(), name="home-page"),
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import AboutSectionAPIView, BlueprintAPIView, FeatureListAPIView, HeroSectionViewSet, BannerStatListAPIView, TestimonialListAPIView,TestimonialSectionAPIView, WhyChooseUsAPIView

# router = DefaultRouter()
# router.register("herosection", HeroSectionViewSet, basename="herosection")

# urlpatterns = [
#     path("", include(router.urls)),  # router URLs for HeroSection
#     path("bannerstats/", BannerStatListAPIView.as_view(), name="bannerstats"),  
#     path("about/", AboutSectionAPIView.as_view(), name="about-section"),
#     path("features/", FeatureListAPIView.as_view(), name='features'),
#     path("why-choose-us/", WhyChooseUsAPIView.as_view(), name='why-choose-us'),
#       path('blueprint/', BlueprintAPIView.as_view(), name='blueprint'),
#        path("testimonials/section/", TestimonialSectionAPIView.as_view(), name="testimonial-section"),
#     path("testimonials/", TestimonialListAPIView.as_view(), name="testimonials"),
# ]
