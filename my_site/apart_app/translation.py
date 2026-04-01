from .models import Country, City, Region, District, Condition, Property, Review
from modeltranslation.translator import TranslationOptions, register


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'property_type')


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('region_name',)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('district_name',)


@register(Condition)
class ConditionTranslationOptions(TranslationOptions):
    fields = ('condition_name',)