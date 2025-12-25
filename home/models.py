from django.db import models

class HeroSection(models.Model):
    subtitle = models.CharField(max_length=100)
    main_title = models.CharField(max_length=200)
    title_1 = models.CharField(max_length=200)
    description = models.TextField()
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        # Force single row (always ID = 1)
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
       return self.main_title

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

class BannerStat(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    suffix = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.label} - {self.value}{self.suffix or ''}"

class AboutSection(models.Model):
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField() 

    
    # Image label and text
    img_label = models.CharField(max_length=255, blank=True, null=True)
    img_text = models.CharField(max_length=255, blank=True, null=True)

    # Image for left section
    image = models.ImageField(upload_to="about_images/", blank=True, null=True)

    def __str__(self):
        return self.title
    
class AboutStat(models.Model):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name="stats")
    label = models.CharField(max_length=50)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label} - {self.text}"