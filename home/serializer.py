# home/serializers.py
from rest_framework import serializers
from .models import (
    HeroSection,
    BannerStat,
    AboutSection,
    AboutStat,
    Feature,
    WhyChooseUs,
    WhyChooseUsPoint,
    Blueprint,
    BlueprintProcess,
    TestimonialSection,
    Testimonial,
)


class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class BannerStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerStat
        fields = '__all__'




class AboutStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutStat
        fields = ("id", "label", "text")


class AboutSectionSerializer(serializers.ModelSerializer):
    stats = AboutStatSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = AboutSection
        fields = (
            "id",
            "region",
            "subtitle",
            "title",
            "description",
            "image",
            "img_label",
            "img_text",
            "stats",
        )

    def get_image(self, obj):
        return obj.image.url if obj.image else None

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ("id", "title", "description", "icon")


class WhyChooseUsPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUsPoint
        fields = ("id", "point")


class WhyChooseUsSerializer(serializers.ModelSerializer):
    points = WhyChooseUsPointSerializer(many=True, read_only=True)

    class Meta:
        model = WhyChooseUs
        fields = (
            "id",
            "region",
            "subtitle",
            "title",
            "description",
            "points",
        )


class TestimonialSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = (
            "id",
            "author",
            "position",
            "company",
            "text",
            "image",
        )

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    def get_image(self, obj):
        return obj.image.url if obj.image else None


class TestimonialSectionSerializer(serializers.ModelSerializer):
    testimonials = serializers.SerializerMethodField()

    class Meta:
        model = TestimonialSection
        fields = (
            "id",
            "region",
            "subtitle",
            "title",
            "title_1",
            "description",
            "testimonials",
        )

    def get_testimonials(self, obj):
        testimonials = Testimonial.objects.all()
        return TestimonialSerializer(testimonials, many=True).data
    
class BlueprintProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlueprintProcess
        fields = ("id", "number", "title", "description")


class BlueprintSerializer(serializers.ModelSerializer):
    process = BlueprintProcessSerializer(many=True, read_only=True)

    class Meta:
        model = Blueprint
        fields = (
            "id",
            "region",
            "title",
            "subtitle",
            "description",
            "process",
        )
