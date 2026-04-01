from django_filters.rest_framework import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'country' : ['exact'],
            'city' : ['exact'],
            'region':['exact'],
            'price' : ['lt', 'gt'],
            'district' : ['exact'],
            'rooms': ['lt', 'gt'],
            'total_floors':['lt', 'gt'],
        }