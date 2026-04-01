from django.contrib import admin
from .models import (
    UserProfile, Country, City, Region,
    District, Condition, PropertyImage, Property, Review
)
from modeltranslation.admin import TranslationAdmin


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


@admin.register(Property)
class PropertyAdmin(TranslationAdmin):
    inlines = [PropertyImageInline, ReviewInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Condition)
admin.site.register(Review)