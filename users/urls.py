from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.apps import UsersConfig

from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDeleteAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-get'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #получение токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #обновление токена
]
