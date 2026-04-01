from django.urls import include, path
from rest_framework.routers import DefaultRouter,SimpleRouter
from .views import *

router = SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('property/', PropertyListAPIView.as_view(), name='property_list'),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view(), name='property_detail'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('region/', RegionListAPIView.as_view(), name='region_list'),
    path('district/', DistrictListAPIView.as_view(), name='district_list'),
    path('condition/', ConditionListAPIView.as_view(), name='condition_list'),
    path('review/', ReviewListAPIView.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review_detail'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('review/<int:pk>/update/', ReviewUpdateAPIView.as_view(), name='review_update'),
]