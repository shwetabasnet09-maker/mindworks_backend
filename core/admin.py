# from django.contrib import admin
# from unfold.admin import ModelAdmin, TabularInline
# from .models import Product, Service, ProjectPost, ProjectPostImage, ServiceTimeline
# from ckeditor.widgets import CKEditorWidget
# from django import forms
# from django.utils.html import format_html


 
# class ServiceAdminForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorWidget())
#     features = forms.CharField(widget=CKEditorWidget())

#     class Meta:
#         model = Service
#         fields = "__all__"

# # ---------------- Timeline Inline ----------------
# class ServiceTimelineInline(admin.TabularInline):
#     model = ServiceTimeline
#     extra = 1
#     verbose_name = "Timeline Step"
#     verbose_name_plural = "Timeline Steps"

# @admin.register(Service)
# class ServiceAdmin(ModelAdmin):
#     form = ServiceAdminForm
#     list_display = ("id", "title", "slug", "is_active")
#     list_display_links = ("title",)
#     list_filter = ("is_active",)
#     search_fields = ("title", "slug")
#     prepopulated_fields = {"slug": ("title",)}
#     inlines = [ServiceTimelineInline] 
    
# class ProjectPostImageInline(admin.TabularInline):
#     model = ProjectPostImage
#     extra = 1

#     fields = ("image", "image_preview", "alt_text")
#     readonly_fields = ("image_preview",)

#     def image_preview(self, obj):
#         if obj.image:
#             return format_html(
#                 '<img src="{}" style="height: 100px; object-fit: cover; border-radius: 6px;" />',
#                 obj.image.url
#             )
#         return "-"

#     image_preview.short_description = "Preview"


# class ProjectPostAdminForm(ModelAdmin):
#      content = forms.CharField(widget=CKEditorWidget())

# class Meta:
#         model = ProjectPost
#         fields = "__all__"


# @admin.register(ProjectPost)
# class ProjectPostAdmin(ModelAdmin):
#     form = ProjectPostAdminForm

#     list_display = ("title", "is_active", "created_at")
#     list_filter = ("is_active",)
#     search_fields = ("title",)
#     prepopulated_fields = {"slug": ("title",)}

#     inlines = [ProjectPostImageInline]

#     readonly_fields = ("banner_preview", "feature_preview")

#     fields = (
#         "title",
#         "slug",
#         "content",
#         "banner_img",
#         "banner_preview",
#         "feature_img",
#         "feature_preview",
#         "is_active",
#     )

#     def banner_preview(self, obj):
#         if obj.banner_img:
#             return format_html(
#                 '<img src="{}" style="height: 150px; object-fit: cover; border-radius: 8px;" />',
#                 obj.banner_img.url
#             )
#         return "-"

#     def feature_preview(self, obj):
#         if obj.feature_img:
#             return format_html(
#                 '<img src="{}" style="height: 120px; object-fit: cover; border-radius: 8px;" />',
#                 obj.feature_img.url
#             )
#         return "-"

#     banner_preview.short_description = "Banner Preview"
#     feature_preview.short_description = "Feature Preview"


from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Blog, Product, Service, ProjectPost, ProjectPostImage, ServiceTimeline, Blog, Category, ContactSubmission
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.utils.html import format_html


# ---------------- Service Admin ----------------
class ServiceAdminForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditorWidget(), required=False)
    short_description = forms.CharField(widget=CKEditorWidget(), required=False)
    features = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Service
        fields = "__all__"


class ServiceTimelineInline(TabularInline):
    model = ServiceTimeline
    extra = 1
    verbose_name = "Timeline Step"
    verbose_name_plural = "Timeline Steps"
    fields = ("title", "short_description")


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    form = ServiceAdminForm
    list_display = ("id", "title", "slug", "is_active")
    list_display_links = ("title",)
    list_filter = ("is_active",)
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ServiceTimelineInline]


# ---------------- ProjectPost Admin ----------------
class ProjectPostImageInline(TabularInline):
    model = ProjectPostImage
    extra = 1
    fields = ("image", "image_preview", "alt_text")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 100px; object-fit: cover; border-radius: 6px;" />',
                obj.image.url
            )
        return "-"

    image_preview.short_description = "Preview"


class ProjectPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = ProjectPost
        fields = "__all__"


@admin.register(ProjectPost)
class ProjectPostAdmin(ModelAdmin):
    form = ProjectPostAdminForm

    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectPostImageInline]

    readonly_fields = ("banner_preview", "feature_preview")

    fields = (
        "title",
        "slug",
        "content",
        "banner_img",
        "banner_preview",
        "feature_img",
        "feature_preview",
        "is_active",
        "image",
    )

    def banner_preview(self, obj):
        if obj.banner_img:
            return format_html(
                '<img src="{}" style="height: 150px; object-fit: cover; border-radius: 8px;" />',
                obj.banner_img.url
            )
        return "-"

    def feature_preview(self, obj):
        if obj.feature_img:
            return format_html(
                '<img src="{}" style="height: 120px; object-fit: cover; border-radius: 8px;" />',
                obj.feature_img.url
            )
        return "-"

    banner_preview.short_description = "Banner Preview"
    feature_preview.short_description = "Feature Preview"


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


# ---------------- BLOG ADMIN ----------------
@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ("id", "title", "category", "image_preview", "date")
    list_filter = ("category", "date")
    search_fields = ("title", "excerpt", "content")

    # ❌ REMOVE date from readonly
    readonly_fields = ("image_preview",)

    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        ("Main Info", {
            "fields": ("title", "category", "slug", "date"),
        }),
        ("Content", {
            "fields": ("excerpt", "content"),
            "classes": ("collapse",),
        }),
        ("Media", {
            "fields": ("image", "image_preview"),
            "classes": ("collapse",),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:100px;border-radius:6px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Preview"

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(ModelAdmin):
   
    list_display = ('name', 'email', 'subject', 'company', 'created_at')
    
   
    list_display_links = ('name', 'email')
    
    
    list_filter = ('created_at', 'company')
    
    
    search_fields = ('name', 'email', 'subject', 'message')
    
   
    readonly_fields = ('created_at',)
    

    ordering = ('-created_at',)
    
    
    list_per_page = 20

    
    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'company', 'phone', 'email')
        }),
        ('Message Details', {
            'fields': ('subject', 'message')
        }),
        ('System Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )