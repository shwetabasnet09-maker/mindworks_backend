# home/serializers.py
from rest_framework import serializers
from .models import AboutSection, AboutStat, HeroSection, BannerStat

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
        fields = ["label", "text"]

class AboutSectionSerializer(serializers.ModelSerializer):
    stats = AboutStatSerializer(many=True, read_only=True)

    class Meta:
        model = AboutSection
        fields = [
            "subtitle",
            "title",
            "description",   # just the model field name
            "image",
            "img_label",
            "img_text",
            "stats",
        ]