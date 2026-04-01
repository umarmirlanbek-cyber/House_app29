<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CharField, ForeignKey
from phonenumber_field.formfields import PhoneNumberField


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('seller', 'seller'),
        ('buyer', 'buyer'),
    )
    phone_number = PhoneNumberField()
    role = models.CharField(choices=ROLE_CHOICES, default='guest', max_length=32)


class Country(models.Model):
    country_name = models.CharField(max_length=64)
    country_image = models.ImageField(upload_to='country_photo/')

    def __str__(self):
        return f'{self.country_name} {self.country_image}'


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_cities')
    city_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.city_name


class Region(models.Model):
    region_name = CharField(max_length=128, unique=True)
    city = ForeignKey(City, on_delete=models.CASCADE, related_name='city_regions')

    def __str__(self):
        return self.region_name


class District(models.Model):
    district_name = models.CharField(max_length=128, unique=True)
    region = ForeignKey(Region, on_delete=models.CASCADE, related_name='region_districts')

    def __str__(self):
        return self.district_name


class Condition(models.Model):
    condition_name = models.CharField(max_length=32)

    def __str__(self):
        return self.condition_name


class Property(models.Model):
    title = models.CharField(max_length=128)
    PROPERTY_TYPE = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('commercial property', 'commercial property'),
        ('rooms', 'rooms'),
        ('parking/garage', 'parking/garage'),
        ('country house', 'country house'),
    )
    property_type = models.CharField(unique=True, choices=PROPERTY_TYPE, max_length=32)
    region = ForeignKey(Region, on_delete=models.CASCADE, related_name='region_properties')
    city = ForeignKey(City, on_delete=models.CASCADE, related_name='city_properties')
    country = ForeignKey(Country, on_delete=models.CASCADE, related_name='country_properties')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_properties')
    area = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    price = models.PositiveSmallIntegerField()
    rooms = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                             null=True, blank=True)
    floor = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
                                             null=True, blank=True)
    total_floors = models.PositiveSmallIntegerField()
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='condition_properties')
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='seller_properties')

    def get_avg_rating(self):
        rating = self.property_review.all()
        if rating.exists():
            return round(sum(i.star for i in rating) / rating.count(), 2)
        return 0

    def get_count_people(self):
        return self.property_review.count()


class PropertyImage(models.Model):
    property_image = models.ImageField(upload_to='photo_property/')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images', null=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_reviews')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_review')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                              null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.property)
>>>>>>> rakanbek
