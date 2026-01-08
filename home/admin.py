from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Blueprint, BlueprintProcess, Feature, HeroSection, BannerStat, AboutSection, AboutStat, TestimonialSection, WhyChooseUs, WhyChooseUsPoint, Testimonial
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse



@admin.register(HeroSection)
class HeroSectionAdmin(ModelAdmin):
    list_display = ("region", "main_title")
    list_filter = ("region",)

    fieldsets = (
        ("Region", {
            "fields": ("region",)
        }),
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


    

@admin.register(BannerStat)
class BannerStatAdmin(ModelAdmin):
    list_display = ("region", "label", "value", "suffix")
    list_filter = ("region",)
    search_fields = ("label",)

class AboutSectionAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AboutSection
        fields = "__all__"




class AboutStatInline(TabularInline):
    model = AboutStat
    extra = 1




@admin.register(AboutSection)
class AboutSectionAdmin(ModelAdmin):
    form = AboutSectionAdminForm
    inlines = [AboutStatInline]

    list_display = ("region", "title")
    list_filter = ("region",)

    fieldsets = (
        ("Region", {
            "fields": ("region",)
        }),
        ("Content", {
            "fields": (
                "subtitle",
                "title",
                "description",
                "img_label",
                "img_text",
                "image",
            )
        }),
    )

@admin.register(Feature)
class FeatureAdmin(ModelAdmin):
    list_display = ("title", "icon")
    search_fields = ("title",)

class WhyChooseUsPointInline(TabularInline):
    model = WhyChooseUsPoint
    extra = 1


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(ModelAdmin):
    list_display = ("region", "title")
    list_filter = ("region",)
    inlines = [WhyChooseUsPointInline]

class BlueprintProcessInline(TabularInline):
    model = BlueprintProcess
    extra = 1

@admin.register(Blueprint)
class BlueprintAdmin(ModelAdmin):
    list_display = ("region", "title")
    list_filter = ("region",)
    inlines = [BlueprintProcessInline]


@admin.register(TestimonialSection)
class TestimonialSectionAdmin(ModelAdmin):
    list_display = ("region", "title")
    list_filter = ("region",)

    fieldsets = (
        ("Region", {
            "fields": ("region",)
        }),
        ("Section Content", {
            "fields": (
                "subtitle",
                "title",
                "title_1",
                "description",
            )
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ("author", "company", "position")
    search_fields = ("author", "company")
    list_filter = ("company",)
