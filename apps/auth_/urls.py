from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import EmailActivate
from .views import RegisterView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='tokens'),
    path('activate/', EmailActivate.as_view(), name='activate_email'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('register/', RegisterView.as_view(), name='register_user')
]
