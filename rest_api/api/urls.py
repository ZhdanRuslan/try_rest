from django.urls import include, path
from rest_auth.registration.views import VerifyEmailView, RegisterView

urlpatterns = [
    path('users/', include('users.urls')),
    path('shop/', include('shop.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('rest-auth/logout/', include('rest_auth.urls')),
    path('rest-auth/user/', include('rest_auth.urls')),


    path('rest-auth/', include('rest_auth.urls')),

    # path('rest-auth/registration/', RegisterView.as_view(), name='signup'),
]
