from django.db import models
from django.core.exceptions import ValidationError

REGION_CHOICES = (
    ("global", "Global"),
    ("ae", "UAE"),
)
class HeroSection(models.Model):
    region = models.CharField(
        max_length=10,
        choices=REGION_CHOICES,
        default="global",
        unique=True
    )

    subtitle = models.CharField(max_length=100)
    main_title = models.CharField(max_length=200)
    title_1 = models.CharField(max_length=200)
    description = models.TextField()
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.region.upper()} Hero"

class BannerStat(models.Model):
    region = models.CharField(
        max_length=10,
        choices=REGION_CHOICES,
        default="global"
    )

    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    suffix = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.region.upper()} - {self.label}"


class AboutSection(models.Model):
    region = models.CharField(
        max_length=10,
        choices=REGION_CHOICES,
        default="global",
        unique=True
    )

    subtitle = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    img_label = models.CharField(max_length=255, blank=True, null=True)
    img_text = models.CharField(max_length=255, blank=True, null=True)

    image = models.ImageField(upload_to="about_images/", blank=True, null=True)

    def __str__(self):
        return f"{self.region.upper()} About"

    
class AboutStat(models.Model):
    about_section = models.ForeignKey(
        AboutSection,
        on_delete=models.CASCADE,
        related_name="stats"
    )
    label = models.CharField(max_length=50)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label} - {self.text}"


class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(
        max_length=100,
        help_text="Icon name (e.g., BarChart3)"
    )

    def __str__(self):
        return self.title

class WhyChooseUs(models.Model):
    region = models.CharField(
        max_length=10,
        choices=REGION_CHOICES,
        default="global",
        unique=True
    )

    subtitle = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.region.upper()} Why Choose Us"

class WhyChooseUsPoint(models.Model):
    why_choose_us = models.ForeignKey(
        WhyChooseUs,
        related_name="points",
        on_delete=models.CASCADE
    )
    point = models.TextField()

    def __str__(self):
        return self.point[:40]



class Blueprint(models.Model):
    region = models.CharField(
        max_length=10,
        choices=REGION_CHOICES,
        default="global",
        unique=True
    )

    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.region.upper()} Blueprint"
class BlueprintProcess(models.Model):
    blueprint = models.ForeignKey(
        Blueprint,
        related_name="process",
        on_delete=models.CASCADE
    )
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.number} - {self.title}"

class TestimonialSection(models.Model):
    region = models.CharField(
        max_length=10,
        choices=REGION_CHOICES,
        default="global",
        unique=True
    )

    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_1 = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.region.upper()} Testimonials"



class Testimonial(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.author
