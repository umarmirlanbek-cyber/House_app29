from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserProfile, Country, City, Region, District, Condition, PropertyImage, Property, Review


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'role']


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'role']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class CityListSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ['id', 'country', 'city_name']


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'region_name']


class RegionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'district_name']


class DistrictNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['district_name']


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ['condition_name']



class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    created_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Review
        fields = ['id', 'user', 'comment', 'rating', 'created_date']


class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    created_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Review
        fields = ['user', 'comment', 'rating', 'created_date']


class PropertyListSerializer(serializers.ModelSerializer):
    property_image = PropertyImageSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()
    city = CityNameSerializer()
    country = CountrySerializer()

    class Meta:
        model = Property
        fields = ['id', 'title', 'property_image', 'price',
                  'rooms', 'floor', 'area', 'city', 'country',
                  'avg_rating', 'count_review']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_review(self, obj):
        return obj.get_count_people()


class PropertyDetailSerializer(serializers.ModelSerializer):
    property_image = PropertyImageSerializer(many=True, read_only=True)
    property_review = ReviewListSerializer(many=True, read_only=True)
    city = CityNameSerializer()
    country = CountrySerializer()
    region = RegionNameSerializer()
    district = DistrictNameSerializer()
    condition = ConditionSerializer()
    seller = UserProfileNameSerializer()
    avg_rating = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ['id', 'title', 'property_image', 'property_type',
                  'country', 'city', 'region', 'district',
                  'area', 'price', 'rooms', 'floor', 'total_floors',
                  'condition', 'seller', 'avg_rating', 'count_review',
                  'property_review']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_review(self, obj):
        return obj.get_count_people()


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }