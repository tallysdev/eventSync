from django.urls import path
from .views import ApiRootView

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
]