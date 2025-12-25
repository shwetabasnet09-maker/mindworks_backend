# home/views.py
from rest_framework import viewsets
from .models import HeroSection, BannerStat, AboutSection
from rest_framework import generics
from .serializer import HeroSectionSerializer, BannerStatSerializer, AboutSectionSerializer

class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer

class BannerStatListAPIView(generics.ListAPIView):
    queryset = BannerStat.objects.all()
    serializer_class = BannerStatSerializer


class AboutSectionAPIView(generics.RetrieveAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

    def get_object(self):
        return self.queryset.first()  