# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# from .views import  ProductViewSet, ServiceViewSet, ProjectPostListAPIView, ProjectPostDetailAPIView

# router = DefaultRouter()
# router.register("products", ProductViewSet)


# router.register("services", ServiceViewSet, basename="services")

# urlpatterns = [
#   path('', include(router.urls)),
 
#     # ProjectPost list and detail views as APIViews
#     path("project-posts/", ProjectPostListAPIView.as_view(), name="projectpost-list"),
#     path("project-posts/<slug:slug>/", ProjectPostDetailAPIView.as_view(), name="projectpost-detail"),
# ]
# urlpatterns = router.urls

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryListView,
    BlogDetailView,
    BlogListView,
    ContactInfoListAPIView,
    ProductViewSet,
    ServiceViewSet,
    ProjectPostListAPIView,
    ProjectPostDetailAPIView,
    ContactCreateView,
    TeamMemberDetailView,
    TeamMemberListView
)

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("services", ServiceViewSet, basename="services")

urlpatterns = [
    path("", include(router.urls)),

    # ProjectPost list and detail views
    path("project-posts/", ProjectPostListAPIView.as_view(), name="projectpost-list"),
    path("project-posts/<slug:slug>/", ProjectPostDetailAPIView.as_view(), name="projectpost-detail"),
     path("categories/", CategoryListView.as_view(), name="category-list"),
    path("blogs/", BlogListView.as_view(), name="post-list"),
    path("blogs/<str:link>/", BlogDetailView.as_view(), name="post-detail"),
    path("contact/", ContactCreateView.as_view(), name="contact-submit"),
    path("team/", TeamMemberListView.as_view(), name="team-list"),
    path("team/<int:id>/", TeamMemberDetailView.as_view(), name="team-detail"),
    path("contact-info/", ContactInfoListAPIView.as_view(), name="contact-info"),
    
]
