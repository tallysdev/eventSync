from django.urls import path
from .views import ApiRootView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
]

# auth urls 
urlpatterns += [
    # path('register', user.createAccount, name='createAccount'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]