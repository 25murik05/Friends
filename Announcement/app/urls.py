from django.urls import path
from .views import RegistrationAPIView


app_name = 'app'


urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/<int:pk>', RegistrationAPIView.as_view()),
]