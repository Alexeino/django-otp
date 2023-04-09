from django.urls import path
from .views import RegisterAV, ValidateOTPAV
urlpatterns = [
    path('register/',RegisterAV.as_view(),name="register_user"),
    path('verify_mobile/',ValidateOTPAV.as_view(),name="verify_mobile")
]
