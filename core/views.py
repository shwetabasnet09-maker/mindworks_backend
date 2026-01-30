# from rest_framework.viewsets import ModelViewSet
# from rest_framework import generics
# from .models import  Category, Blog, Product,Service, ProjectPost
# from .serializer import BlogSerializer, CategorySerializer, BlogSerializer, ProductSerializer, ServiceSerializer, ProjectPostSerializer, ContactSubmissionSerializer
# from rest_framework.generics import ListAPIView, RetrieveAPIView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ServiceViewSet(ModelViewSet):
#     queryset = Service.objects.filter(is_active=True)
#     serializer_class = ServiceSerializer
#     lookup_field = "slug"

# # class ProjectPostListAPIView(ListAPIView):
# #     queryset = ProjectPost.objects.prefetch_related("images")
# #     serializer_class = ProjectPostSerializer


# # class ProjectPostDetailAPIView(RetrieveAPIView):
# #     queryset = ProjectPost.objects.prefetch_related("images")
# #     serializer_class = ProjectPostSerializer
# #     lookup_field = "slug"

# class ProjectPostListAPIView(ListAPIView):
#     queryset = ProjectPost.objects.all()
#     serializer_class = ProjectPostSerializer

# class ProjectPostDetailAPIView(RetrieveAPIView):
#     queryset = ProjectPost.objects.all()
#     serializer_class = ProjectPostSerializer
#     lookup_field = 'slug'

# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# # List all blogs
# class BlogListView(generics.ListAPIView):
#     queryset = Blog.objects.all().order_by('-date')
#     serializer_class = BlogSerializer

# # Retrieve single blog   by link
# class BlogDetailView(generics.RetrieveAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = 'link'

# class ContactCreateView(APIView):
#     def post(self, request):
#         serializer = ContactSubmissionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Message received!"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Category,
    Blog,
    ContactInfo,
    Product,
    Service,
    ProjectPost,
    TeamMember,
)

from .serializer import (
    BlogSerializer,
    CategorySerializer,
    ProductSerializer,
    ServiceSerializer,
    ProjectPostSerializer,
    ContactSubmissionSerializer,
    TeamMemberSerializer,
    ContactInfoSerializer,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    lookup_field = "slug"


class ProjectPostListAPIView(ListAPIView):
    queryset = ProjectPost.objects.filter(is_active=True)
    serializer_class = ProjectPostSerializer


class ProjectPostDetailAPIView(RetrieveAPIView):
    queryset = ProjectPost.objects.filter(is_active=True)
    serializer_class = ProjectPostSerializer
    lookup_field = "slug"


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogListView(ListAPIView):
    queryset = Blog.objects.all().order_by("-date")
    serializer_class = BlogSerializer


class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "link"


class ContactCreateView(APIView):
    def post(self, request):
        serializer = ContactSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Message received!"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamMemberListView(ListAPIView):
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
class TeamMemberDetailView(RetrieveAPIView):
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
    lookup_field = "id"

class ContactInfoListAPIView(APIView):
    def get(self, request):
        queryset = ContactInfo.objects.filter(is_active=True)
        serializer = ContactInfoSerializer(queryset, many=True)
        return Response(serializer.data)
class ContactInfoDetailAPIView(RetrieveAPIView):
    queryset = ContactInfo.objects.filter(is_active=True)
    serializer_class = ContactInfoSerializer
    lookup_field = "id"
