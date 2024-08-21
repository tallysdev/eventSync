from django.urls import path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework_simplejwt import views as jwt_views

from .views import auth_view as authv
from .views import users_view as userv
from .views.root_view import ApiRootView
from .views import locals_view as locv
from .views import event_view as evtview
from .views import sponsor_view as spview
from .views import sponsorship_view as spsview
from .views import form_view as formview
from .views import question_view as qview
from .views import registration_presence_view as rpview

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('users/', userv.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', userv.UserDetail.as_view(), name='user_detail'),
    path('locals/', locv.LocalListView.as_view(), name='local_list'),
    path('locals/<int:pk>/', locv.LocalDetailView.as_view(), name='local_detail'),
    path('events/', evtview.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', evtview.EventDetailView.as_view(), name='event_detail'),
    path('sponsors/', spview.SponsorListView.as_view(), name='sponsor_list'),
    path('sponsors/<int:pk>/', spview.SponsorDetailView.as_view(),
         name='sponsor_detail'),
    path('sponsorships/', spsview.SponsorShipListView.as_view(),
         name='sponsorship_list'),
    path('sponsorships/<int:pk>/',
         spsview.SponsorShipDetailView.as_view(), name='sponsorship_detail'),
     path('forms/', formview.FormsRegisterList.as_view(), name='form_list'),
     path('forms/<int:pk>/', formview.FormsRegisterDetail.as_view(), name='forms_detail'),
     path('questions/', qview.QuestionList.as_view(), name='question_list'),
     path('questions/<int:pk>/', qview.QuestionDetail.as_view(), name='question_detail'),
     path('events/registration/', rpview.RegistrationPresenceList.as_view(), name='event_registration_list'),
     path('events/registration/<int:event_id>/<int:user_id>/', rpview.RegistrationPresenceDetail.as_view(), name='event_registration_detail'),
     path('eventsorganized/', evtview.UserOrganizedEventsView.as_view(), name='events_organized'),
     path('eventspresence/', evtview.UserPresentEventsView.as_view(), name='events_presence'),
]

# auth urls
urlpatterns += [
    path('register/', authv.RegisterView.as_view(), name='register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

# doc urls
urlpatterns += [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
