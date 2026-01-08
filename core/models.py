from django.utils.timezone import now

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    features = models.TextField(blank=True, null=True, help_text="List of key features")  
    icon = models.CharField(max_length=50, help_text="Lucide icon name e.g. Megaphone")
    img = models.ImageField(upload_to="services/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)




# class ServiceTimeline(models.Model):
#     service = models.ForeignKey(
#         Service,
#         on_delete=models.CASCADE,
#         related_name="timeline"
#     )
#     title = models.CharField(max_length=150)

   
#     short_description = models.CharField(max_length=255)

#     long_description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.title}"


class Service(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    short_description = models.CharField( max_length=255,
    blank=True,
    default="")
    long_description = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ServiceTimeline(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="timeline"
    )
    title = models.CharField(max_length=150)
    short_description = models.CharField( max_length=255,
        blank=True,
        default="")
    long_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title



class ProjectPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    banner_img = models.ImageField(
        upload_to="projects/banners/",
        blank=True,
        null=True
    )
    feature_img = models.ImageField(
        upload_to="projects/features/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProjectPostImage(models.Model):
    project_post = models.ForeignKey(ProjectPost, on_delete=models.CASCADE, 
        related_name="gallery_images")
    image = models.ImageField(upload_to="project/")
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project_post.title}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = RichTextField(blank=True, null=True)
    content = RichTextField()
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    date = models.DateField(default=now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
       
        if not self.link:
            self.link = f"/blog/{self.slug}/"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"