from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import auth_view as authv
from .views import users_view as userv
from .views.root_view import ApiRootView

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('users/', userv.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', userv.UserDetail.as_view(), name='user_detail')
]

# auth urls 
urlpatterns += [
    path('register/', authv.RegisterView.as_view(), name='register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]