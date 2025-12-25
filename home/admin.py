from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import HeroSection, BannerStat, AboutSection, AboutStat
from ckeditor.widgets import CKEditorWidget
from django import forms


@admin.register(HeroSection)
class HeroSectionAdmin(ModelAdmin):
    fieldsets = (
        ("Hero Content", {
            "fields": (
                "subtitle",
                "main_title",
                "title_1",
                "description",
            )
        }),
        ("Button", {
            "fields": (
                "button_text",
                "button_link",
            )
        }),
    )

    def has_add_permission(self, request):
        return not HeroSection.objects.exists()

@admin.register(BannerStat)
class BannerStatAdmin(ModelAdmin):
    list_display = ('label', 'value', 'suffix')
    search_fields = ('label',)

class AboutSectionAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AboutSection
        fields = "__all__"

class AboutStatInline(admin.TabularInline):
    model = AboutStat
    extra = 1

@admin.register(AboutSection)
class AboutSectionAdmin(ModelAdmin):
    form = AboutSectionAdminForm
    inlines = [AboutStatInline]
    list_display = ("title", "subtitle")