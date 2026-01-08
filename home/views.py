# # # home/views.py
# # from rest_framework import viewsets
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from .models import Blueprint, Feature, HeroSection, BannerStat, AboutSection, Testimonial, TestimonialSection, WhyChooseUs
# # from rest_framework import generics
# # from rest_framework import status
# # from .serializer import BlueprintSerializer, FeatureSerializer, HeroSectionSerializer, BannerStatSerializer, AboutSectionSerializer, TestimonialSectionSerializer, TestimonialSerializer, WhyChooseUsSerializer

# # class HeroSectionViewSet(viewsets.ModelViewSet):
# #     queryset = HeroSection.objects.all()
# #     serializer_class = HeroSectionSerializer

# # class BannerStatListAPIView(generics.ListAPIView):
# #     queryset = BannerStat.objects.all()
# #     serializer_class = BannerStatSerializer


# # class AboutSectionAPIView(generics.RetrieveAPIView):
# #     queryset = AboutSection.objects.all()
# #     serializer_class = AboutSectionSerializer

# #     def get_object(self):
# #         return self.queryset.first()  
    
# # class FeatureListAPIView(generics.ListAPIView):
# #     queryset = Feature.objects.all()
# #     serializer_class = FeatureSerializer

# # class WhyChooseUsAPIView(generics.ListAPIView):
# #     queryset = WhyChooseUs.objects.prefetch_related('points').all()
# #     serializer_class = WhyChooseUsSerializer

# # class BlueprintAPIView(generics.ListAPIView):
# #     queryset = Blueprint.objects.prefetch_related('process').all()
# #     serializer_class = BlueprintSerializer

# # class TestimonialSectionAPIView(APIView):
# #     def get(self, request):
# #         section = TestimonialSection.objects.first()
# #         if not section:
# #             return Response({"detail": "Section not found"}, status=status.HTTP_404_NOT_FOUND)

      
# #         serializer = TestimonialSectionSerializer(section, context={"request": request})
# #         return Response(serializer.data)


# # class TestimonialListAPIView(APIView):
# #     def get(self, request):
# #         testimonials = Testimonial.objects.all()
# #         serializer = TestimonialSerializer(testimonials, many=True, context={"request": request})
# #         return Response(serializer.data)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Feature, HeroSection, BannerStat, AboutSection, WhyChooseUs, Blueprint, Testimonial  
# from .serializer import HeroSectionSerializer, BannerStatSerializer, AboutSectionSerializer, FeatureSerializer, WhyChooseUsSerializer, BlueprintSerializer, TestimonialSerializer  

# class HomePageAPIView(APIView):
#     """
#     API endpoint that returns homepage data based on the region.
#     """
#     def get(self, request, format=None):
#         region = request.GET.get("region", "global")

#         hero = HeroSection.objects.filter(region=region).first()
#         banner_stats = BannerStat.objects.filter(region=region)
#         about = AboutSection.objects.filter(region=region).first()
#         features = Feature.objects.filter(region=region)
#         why_choose_us = WhyChooseUs.objects.filter(region=region).first()
#         blueprint = Blueprint.objects.filter(region=region).first()
#         testimonials = Testimonial.objects.filter(region=region)

#         return Response({
#             "hero": HeroSectionSerializer(hero).data if hero else {},
#             "banner_stats": BannerStatSerializer(banner_stats, many=True).data,
#             "about": AboutSectionSerializer(about).data if about else {},
#             "features": FeatureSerializer(features, many=True).data,
#             "why_choose_us": WhyChooseUsSerializer(why_choose_us).data if why_choose_us else {},
#             "blueprint": BlueprintSerializer(blueprint).data if blueprint else {},
#             "testimonials": TestimonialSerializer(testimonials, many=True).data,
#         })

# home/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
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
    Testimonial
)
from .serializer import (
    HeroSectionSerializer,
    BannerStatSerializer,
    AboutSectionSerializer,
    AboutStatSerializer,
    FeatureSerializer,
    WhyChooseUsSerializer,
    WhyChooseUsPointSerializer,
    BlueprintSerializer,
    BlueprintProcessSerializer,
    TestimonialSectionSerializer,
    TestimonialSerializer
)

class HomePageAPIView(APIView):
    def get(self, request, format=None):
        # Get region from URL query params (default to 'global')
        region = request.GET.get("region", "global")

        # Fetch models with region filtering
        hero = HeroSection.objects.filter(region=region).first()
        banner_stats = BannerStat.objects.filter(region=region)
        about = AboutSection.objects.filter(region=region).first()
        why_choose_us = WhyChooseUs.objects.filter(region=region).first()
        blueprint = Blueprint.objects.filter(region=region).first()
        testimonials = Testimonial.objects.all()  # TestimonialSection also uses region
        testimonial_section = TestimonialSection.objects.filter(region=region).first()

        # Features are global, no region field
        features = Feature.objects.all()

        return Response({
            "hero": HeroSectionSerializer(hero).data if hero else {},
            "banner_stats": BannerStatSerializer(banner_stats, many=True).data,
            "about": AboutSectionSerializer(about).data if about else {},
            "features": FeatureSerializer(features, many=True).data,
            "why_choose_us": WhyChooseUsSerializer(why_choose_us).data if why_choose_us else {},
            "blueprint": BlueprintSerializer(blueprint).data if blueprint else {},
            "testimonials_section": TestimonialSectionSerializer(testimonial_section).data if testimonial_section else {},
            "testimonials": TestimonialSerializer(testimonials, many=True).data,
        })
