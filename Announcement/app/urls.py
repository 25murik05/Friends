from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserApiView


app_name = 'app'


urlpatterns = [
    path('auth/register/', RegistrationAPIView.as_view()),
    path('auth/login/', LoginAPIView.as_view()),
    path('user/<int:pk>/', UserApiView.as_view()),
]