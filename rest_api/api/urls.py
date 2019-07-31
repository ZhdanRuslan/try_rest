from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('shop/', include('shop.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
