from rest_framework import serializers
from .models import Blog, Category, Blog, Product, ProjectPost, ProjectPostImage, ServiceTimeline
from .models import Service, ContactSubmission


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ServiceTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTimeline
        fields = ("title", "short_description", "long_description")

class ServiceSerializer(serializers.ModelSerializer):
    timeline = ServiceTimelineSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = "__all__"

# class ProjectPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectPost
#         fields = "__all__"

class ProjectPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPostImage
        fields = ["id", "image", "alt_text"]


class ProjectPostSerializer(serializers.ModelSerializer):
    # Use the related_name from ProjectPostImage
    gallery_images = ProjectPostImageSerializer(many=True, read_only=True)
    banner_img = serializers.ImageField(read_only=True)
    feature_img = serializers.ImageField(read_only=True)

    class Meta:
        model = ProjectPost
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "banner_img",
            "feature_img",
            "gallery_images",
            "created_at",
            "updated_at",
            "is_active",
        ]
class CategorySerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "count"]

    def get_count(self, obj):
        # Example: count related posts
        return obj.blog_set.count()  

class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "excerpt","content", "date", "image", "slug", "category"]

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'