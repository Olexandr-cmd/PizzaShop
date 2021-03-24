from django.urls import path

from .views import UserListView, UpToAdminView, UpdateProfileView

urlpatterns = [
    path('', UserListView.as_view(), name='all_users'),
    path('<int:pk>/to_admin/', UpToAdminView.as_view(), name='up_to_admin'),
    path('<int:pk>/profile/', UpdateProfileView.as_view(), name='update_profile')
]
