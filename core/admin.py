from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Product, Service
from ckeditor.widgets import CKEditorWidget
from django import forms


class ServiceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Service
        fields = "__all__"


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ("id", "name", "price")

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    form = ServiceAdminForm
    list_display = ("id", "title", "slug", "is_active")
    list_display_links = ("title",)
    list_filter = ("is_active",)
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}

